#### Give permission to setup_env.sh
```
chmod +x setup_env.sh
```

#### Run File with sudo access
```
sudo sh ./setup_env.sh
```

#### Run Celery
1) pipenv shell
2) celery worker -A main.client --loglevel=info

#### Run Flower
1) pipenv shell
2) flower -A main.client ---port=5555
