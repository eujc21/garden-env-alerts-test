#!/bin/sh         
    
if ! type "redis-cli" > /dev/null; then    
    echo "Please install Redis"                     
    echo "Check out https://redis.io/topics/quickstart"     
    exit 1    
else         
    sudo systemctl restart redis.service    
fi


if ! type "pipenv" > /dev/null; then    
    echo "Please install pipenv"                     
    exit 1    
else         
		pip install pipenv
fi

pipenv --rm
pipenv --three
pipenv install --skip-lock 
export FLASK_APP=main.py
pipenv run flask run --host=0.0.0.0

