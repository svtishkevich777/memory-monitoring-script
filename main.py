import psutil
import requests
import json
import time


url = "http://your-api-address"


def main():

    result_memory = psutil.virtual_memory().percent # Here we get the percentage of memory consumption

    if result_memory >= 90.0:

        payload = json.dumps({"message": "Alarm"})
        requests.request("POST", url, data=payload)  # Here’s a message on the API


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1.5)
