import csv

from generate_values import GenerateValues
from main import send_data_to_aws



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

while True:
    for sensor in sensors:
        send_data_to_aws(sensor.generate())