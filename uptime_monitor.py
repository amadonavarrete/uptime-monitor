# Develop a monitoring script that checks if one or more services are online.
# Logs results with timestamps.
# Send an alert via Slack if a service goes down.

from dotenv import load_dotenv
import os
import requests

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_test_alert():
	message = {
		"text": "*Test Alert*: Slack integration is working!" 
	}
	try: 
		response = requests.post(SLACK_WEBHOOK_URL, json=message)
		if response.status_code == 200:
			print("Slack test alert sent successfully.")
		else:
			print(f"Slack test alert failed: {response.status_code}, {response.text}")
	except Exception as e:
		print(f"Error sending Slack alert: {e}")

send_test_alert()