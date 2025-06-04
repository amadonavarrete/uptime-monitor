![Uptime Monitor Banner](resources/uptime-monitor-banner.png)

## Project Overview
An uptime monitoring utility that performs scheduled service checks, triggers downtime alerts, and maintains logs for performance analysis and response readiness.

This project is designed to simulate real-world system reliability practices by tracking the availability of web services and alerting based on their status. Built with Python and Docker, the script continuously checks the status of specified websites, logs all results to a local file `alerts.log`, and sends real-time notifications to a Slack channel.

Key capabilities include:
- **Automated Uptime Checks** - Repeatedly pings websites at a fixed interval.
- **Real-Time Slack Alerts** - Instantly notifies the status of a web service.
- **Timestamped Logging** - Logs are written with local timestamps for future analysis or ingestion into tools like Splunk.
- **Dockerized for Portability** - Easily deployable and repeatable across environments.
  
Technologies used:
- **Python**
- **Docker**
- **Slack Webhooks**
- **Splunk**

---------------------

## 🔗 Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/amadonavarrete/)
