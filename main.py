import os
from sys import argv
import json
import csv
import request
import redis
from datetime import datetime
from parameters import parameters

# Get file going to parse through.

# Create a celery task with a redis broker to deploy alerts

def main():
    parameters()
    script, file_name = argv
    with open(file_name) as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data = []
        for row in reader:
            data.append(row)

        

if __name__ == "__main__":
    main()
