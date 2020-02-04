from os import environ
from datetime import datetime, timezone, timedelta
from random import randint
import time

from influxdb import InfluxDBClient
from dotenv import load_dotenv


load_dotenv(dotenv_path="py_influx.env")


def get_influxdb_client():
    host = environ.get("INFLUXDB_HOST", "localhost")
    port = int(environ.get("INFLUXDB_PORT", 8086))
    username = environ.get("INFLUXDB_USERNAME", "admin")
    password = environ.get("INFLUXDB_PASSWORD", "admin123")
    db = environ.get("INFLUXDB_DATABASE", "testdb")

    return InfluxDBClient(host, port, username, password, db)


def get_time():
    return datetime.now(tz=timezone(timedelta(hours=5, minutes=30))).isoformat()


def get_random_value():
    return randint(400, 500)


def send(client):
    value = get_random_value()
    json_body = [
        {
            "measurement": "sample_measurement",
            "tags": {
                "some_tag": "some_value"
            },
            "time": get_time(),
            "fields": {
                "user_token": "5299f779-5cbe-4a28-b18c-cc2e5718bfa1",
                "username": "arion",
                "value": value,
            }
        }
    ]

    client.write_points(json_body)
    print(f"sending data...{value}")


def main():
    client = get_influxdb_client()

    while True:
        send(client)
        time.sleep(5)

if __name__ == '__main__':
    main()
