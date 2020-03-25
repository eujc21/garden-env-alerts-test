import os
from sys import argv
import json
import csv
import request
import redis
from datetime import datetime

def main():
    script, file_name = argv
    with open(file_name) as f:
        reader = csv.reader(f)
        next(reader) # skip header
        data = []
        for row in reader:
            print(row)
            data.append(row)

        

if __name__ == "__main__":
    main()
