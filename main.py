# https://github.com/Miserlou/Zappa/issues/1426
#__name__ = '.'.join(__name__.split('/'))
#__package__ = '.'.join('.'.join(__name__.split('/')).split('.')[:-1])

import os
from sys import argv
import json
import csv
import request
import redis
from datetime import datetime
from flask import Flask, request    
from flask_cors import CORS    
from celery import Celery    

# TODO: Fix relative import to use flowers for celery
#from .parameters import parameters

app = Flask(__name__)    
CORS(app)    
    
# Celery Config    
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'    
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'    
app.config['REDIS_URL'] = 'redis://localhost:6379/0'    

# Celery Config
client = Celery(    
        app.name,    
        broker=app.config['CELERY_BROKER_URL']    
)    
client.conf.update(    
        app.config    
)    
    
# Create a celery task with a redis broker to deploy alerts
# Redis Config    
r = redis.Redis(host="localhost", port=6379, db=0)

# [X] Get file going to parse through.
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
    
#def parameters():    
#    for parameter in parameter_list:    
#        print(parameter["key"] == "air_temperature") 

@client.task(name="exceed_air_temp")
def exceeds_air_temp():
    return False

@client.task(name="exceeds_humidity")
def exceeds_humidity():
    return False

@client.task(name="exceeds_co2")
def exceeds_co2():
    return False

@client.task(name="exceeds_ec")
def exceeds_ec():
    return False

@client.task(name="exceeds_ph")
def exceeds_ph():
    return False

@client.task(name="exceeds_watertmp")
def exceeds_ph():
    return False

@client.task(name="out_of_range_logic")
def out_of_range_logic(obj):
    # Format time stamp from unix to MM/DD HH:MM
    newobj = {}
    newobj["timestamp"] = datetime
        .utcfromtimestamp(int(obj[1]))
        .strftime('%m/%d %H:%M')
    
    return newobj

@app.route('/csv', methods=['GET', 'POST'])    
def main():
    file_name = request.args.get('file_name')
    with open(file_name) as f:
        reader = csv.reader(f)
        next(reader) # skip header
        for row in reader:
            out_of_range_logic.apply_async(
                    args=[row],
                    countdown=30
            )
    return "Hello World" 

if __name__ == "__main__":                                
    app.run(debug=True)  
