import read_values, json, requests, os, time
from dotenv import load_dotenv


load_dotenv()
aws_url = os.getenv('AWS_URL')
aws_key = os.getenv('AWS_KEY')
FORCE_ERROR_FREQUENCY = 5
REQUEST_DELAY_SECONDS = 1
request_counter = 0


def should_force_error():
    global request_counter
    request_counter += 1
    return request_counter % FORCE_ERROR_FREQUENCY == 0

def send_data_to_aws(data):
    payload = dict(data)
    if should_force_error():
        payload["force_error"] = True
        print("Flagging request for DLQ test.")
    time.sleep(REQUEST_DELAY_SECONDS)
    print(f"Sending data to AWS: {payload}")
    try:
        response = requests.post(aws_url, json=payload)
        print(response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to AWS: {e}")


if __name__ == "__main__":
    read_values.run()