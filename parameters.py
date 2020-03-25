import sys
import json

parameter_list = [
        {
            "key": "air_temperature",
            "high": 83.0,
            "low": 65.0
        },
        {
            "key": "humidity",
            "high": 45.0,
            "low": 90
        },
        {
            "key": "co2",
            "high":800.0,
            "low": 1300.0
        },
        {
            "key": "ec_range",
            "high": 1000.0,
            "low": 2500
        },
        {
            "key": "ph_range",
            "high": 5.7,
            "low": 7.0
        },
        {
            "key": "water_temp",
            "high": 63.0,
            "low": 83.0
        },
]

def parameters():
    for parameter in parameter_list:
        print(parameter["key"] == "air_temperature")

if __name__ == "__main__":
    parameters()
