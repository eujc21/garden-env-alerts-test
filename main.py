import os
from sys import argv
import json
import csv
import request
import redis
from datetime import datetime
from celery import Celery

#from .parameters import parameters

from flask import Flask, request    
from flask_cors import CORS    
from celery import Celery    
               
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

@client.task(name="out_of_range_logic")
def out_of_range_logic(obj):
	return obj

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
