#!/bin/sh         
    
if ! type "redis-cli" > /dev/null; then    
    echo "Please install Redis"                     
    echo "Check out https://redis.io/topics/quickstart"     
    exit 1    
else         
    sudo systemctl restart redis.service    
fi 

export FLASK_APP=main.py
pipenv run flask run --host=0.0.0.0

