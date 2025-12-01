import read_values, json, requests, os
from dotenv import load_dotenv


load_dotenv()
aws_url = os.getenv('AWS_URL')
aws_key = os.getenv('AWS_KEY')

def send_data_to_aws(data):
    print(f"Sending data to AWS: {data}")
    try:
        response = requests.post(aws_url, json=data)
        print(response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to AWS: {e}")


if __name__ == "__main__":
    read_values.run()