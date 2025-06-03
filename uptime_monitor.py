# Develop a monitoring script that checks if one or more services are online.
# Logs results with timestamps.
# Send an alert via Slack if a service goes down.

from dotenv import load_dotenv
from datetime import datetime
import os
import requests
import pytz


load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
SITE_TO_MONITOR = [
	"https://splunk.com",
	"https://github.com",
	"https://httpstat.us/200",
	"https://httpstat.us/403",
	"https://httpstat.us/500",
]

def get_timestamp():
		local_timezone = pytz.timezone("America/New_York")
		return datetime.now(local_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")

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

def check_website(site):
	try: 
		response = requests.get(site, timeout=5)
		if response.status_code == 200:
			print(f"{site} is up.")
			send_slack_alert(site, "UP")
		else: 
			print(f"{site} returned status code {response.status_code}")
			send_slack_alert(site, "DOWN", f"Status code: {response.status_code}")
	except requests.RequestException as e:
		print(f"Error checking {site}: {e}")
		send_slack_alert(site, "DOWN", str(e))

for website in SITE_TO_MONITOR:
	check_website(website)

