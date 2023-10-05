# GithubZipParsingTelegramBot
___
### Description

Simple and fully asynchronous Telegram bot that can download GitHub repository and return as .zip archive.
___
### Getting Started
#### Running on Local Machine
+ install dependencies using PIP
````
pip3 install -r requirements.txt 
````
+ configure environment variables in `.env` file
+ start bot in virtual environment
````
python run.py
````
#### Launch in Docker
+ configure environment variables in `.env` file
+ building the docker image
````
docker-compose build
````
+ start service
````
docker-compose up -d
````
____
#### Environment variables
| variables       | description                               |
|:----------------|:------------------------------------------|
| `APITOKEN`      | Telegram bot API token                    |
| `REDISHOST`     | hostname or an IP address Redis database  |
| `REDISPORT`     | port from Redis database                  |
| `REDISDB`       | Redis database, 0 by default              |
| `REDISPASSWORD` | Redis database password, empty by default |
____
#### Tech Stack
+  `aiogram`
+ `aiofile`
+ `aiohttp`
+ `fake-useragent`
+ `python-dotenv`
+ `redis`
+ `docker` and `docker-compose`