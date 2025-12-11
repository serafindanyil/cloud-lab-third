import os
import time
import requests

from dotenv import load_dotenv
from read_values import load_sensors_from_csv
from generate_values import generate_data

load_dotenv()

AWS_URL = os.getenv('AWS_URL')
FORCE_ERROR_FREQUENCY = 5
REQUEST_DELAY_SECONDS = 1

request_counter = 0

def should_force_error():
    global request_counter
    request_counter += 1
    return request_counter % FORCE_ERROR_FREQUENCY == 0

def send_data_to_aws(data):
    payload = data.copy()
    
    if should_force_error():
        payload["force_error"] = True
        print("Flagging request for DLQ test.")
        
    time.sleep(REQUEST_DELAY_SECONDS)
    print(f"Sending data to AWS: {payload}")
    
    try:
        response = requests.post(AWS_URL, json=payload)
        print(response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to AWS: {e}")

def main():
    sensors = load_sensors_from_csv('config.csv')
    
    while True:
        for sensor in sensors:
            data = generate_data(sensor)
            send_data_to_aws(data)

if __name__ == "__main__":
    main()
