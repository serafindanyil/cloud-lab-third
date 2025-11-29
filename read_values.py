import os, csv
from dotenv import load_dotenv

from generate_values import GenerateValues
from main import send_data_to_aws

load_dotenv()
aws_url = os.getenv('AWS_URL')
aws_key = os.getenv('AWS_KEY')

sensors = []

with open('config.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        sensor = GenerateValues(
            row["Name"],
            float(row["MaxValue"]),
            float(row["MinValue"]),
            float(row["Interval"]),
            row["Location"]
        )
        sensors.append(sensor)



print(f"Loaded {(sensor.generate())} sensors from configuration.")
while True:
    for sensor in sensors:
        print(sensor.generate())
        send_data_to_aws(sensor.generate())