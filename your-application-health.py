import requests
import time
import logging


logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("web_app_health.log"),
                              logging.StreamHandler()])


APP_URL = "https://jsonplaceholder.typicode.com/posts"
CHECK_INTERVAL = 60  # in seconds

def check_app_health(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            logging.info(f"Application is healthy. Status code: {response.status_code}")
        else:
            logging.warning(f"Application may be experiencing issues. Status code: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Failed to connect to the application. Error: {e}")

def monitor_application(url, interval):
    while True:
        check_app_health(url)
        time.sleep(interval)

if __name__ == "__main__":
    monitor_application(APP_URL, CHECK_INTERVAL)
