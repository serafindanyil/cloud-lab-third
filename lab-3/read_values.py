import csv
from generate_values import create_sensor

def load_sensors_from_csv(file_path):
    sensors = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sensor = create_sensor(
                row["Name"],
                float(row["MaxValue"]),
                float(row["MinValue"]),
                float(row["Interval"]),
                row["Location"]
            )
            sensors.append(sensor)
    return sensors
