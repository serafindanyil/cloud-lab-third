import random
import time
import datetime

def create_sensor(name, max_val, min_val, interval, location):
    return {
        "sensor_type": name,
        "max_value": max_val,
        "min_value": min_val,
        "interval": interval,
        "location": location
    }

def generate_data(sensor):
    value = round(random.uniform(sensor["min_value"], sensor["max_value"]), 2)
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    time.sleep(sensor["interval"])
    
    return {
        "sensor_type": sensor["sensor_type"],
        "value": value,
        "timestamp": timestamp,
        "location": sensor["location"]
    }
