from dotenv import load_dotenv
from datetime import datetime
import os
import requests
import pytz
import time


load_dotenv()

CHECK_INTERVAL = 300
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
SITE_TO_MONITOR = [
	"https://splunk.com",
	"https://github.com",
	"https://spacex.com",
	"https://httpstat.us/200",
	"https://httpstat.us/403",
	"https://httpstat.us/500",
	"https://httpstat.us/random/200,201,403,500-504",
	"https://httpstat.us/random/200,201,403,500-504"
]

def get_timestamp():
		local_timezone = pytz.timezone("America/New_York")
		return datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")

def log_alert(site, status, detail=""):
	timestamp = get_timestamp()
	log_line = f'timestamp={timestamp} site={site} status={status} reason="{detail}"\n'
	with open("alerts.log", "a") as logfile:
		logfile.write(log_line)

def send_slack_alert(site, status, detail=""):
	timestamp = get_timestamp()

	if status == "UP":
		message = {
			"text": f"`{site}` is *UP* and responsive as of `{timestamp}`." 
		}
	else: 
		message = {
			"text": f"*ALERT*: `{site}` is *DOWN* as of `{timestamp}`! {detail}"
		}
	try:	
		response = requests.post(SLACK_WEBHOOK_URL, json=message)
		if response.status_code != 200:
			print(f"Slack alert failed: {response.status_code}, {response.text}")
	except Exception as e:
		print(f"Error sending Slack alert: {e}")

	log_alert(site, status, detail)

def check_website(site):
	try: 
		response = requests.get(site, timeout=5)
		if response.status_code == 200:
			print(f"{site} is up.")
			send_slack_alert(site, "UP", f"Status code: {response.status_code}")
		else: 
			print(f"{site} returned status code {response.status_code}")
			send_slack_alert(site, "DOWN", f"Status code: {response.status_code}")
	except requests.RequestException as e:
		print(f"Error checking {site}: {e}")
		send_slack_alert(site, "DOWN", str(e))

if __name__ == '__main__':
	while True:
		for website in SITE_TO_MONITOR:
			check_website(website)
		time.sleep(CHECK_INTERVAL)

