Application Health Checker
This Python script monitors the health of a application by periodically making HTTP requests to a specified URL and logging the results.

Features
HTTP Status Code Monitoring: Checks if the application returns a valid HTTP status code (e.g., 200 OK).
Logging: Logs the health status of the application to both the console and a log file.
Customizable: Easily configurable with customizable monitoring interval and target URL.
Usage
Ensure you have Python installed on your system.
Install the required dependencies using pip install requests.
Modify the APP_URL variable in the script to point to the URL of the web application you want to monitor.
Run the script using python your-application-health.py.
View the output in the console and the web_app_health.log file.
Configuration
APP_URL: The URL of the web application to monitor.
CHECK_INTERVAL: The interval (in seconds) between health checks.
Example
python
Copy code
import requests
import time
import logging

# Configuration
APP_URL = "http://your-application-url.com"
CHECK_INTERVAL = 60  # in seconds

# Remaining code is omitted for brevity. See the full script for details.
Dependencies
requests: HTTP library for making requests in Python.