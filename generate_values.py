import random, time, datetime


class GenerateValues:
    def __init__(self, sensor_type, max_value, min_value, interval, location):
        self.sensor_type = sensor_type
        self.max_value = max_value
        self.min_value = min_value
        self.interval = interval
        self.location = location

    def generate(self):
        value = round(random.uniform(self.min_value, self.max_value), 2)
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        data = {
            "sensor_type": self.sensor_type,
            "value": value,
            "timestamp": timestamp,
            "location": self.location
        }

        time.sleep(self.interval)
        return data