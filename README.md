# GithubZipParsingTelegramBot
___
### Description

Simple and fully asynchronous Telegram bot that can download GitHub repository and return as .zip archive.
___
### Getting Started
#### Running on Local Machine
+ install dependencies using PIP
````
pip install -r requirements.txt 
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
| variables       | description                             |
|:----------------|:----------------------------------------|
| `BOT_API_TOKEN` | Telegram bot API token                  |
| `REDIS_HOST`    | hostname or an IP address Redis database|
| `REDIS_PORT`    | port from Redis database                |
| `REDIS_DB`      | Redis database                          |
____
#### Tech Stack
+ `aiohttp`
+ `aiogram`
+ `aiofiles`
+ `redis`
+ `docker` and `docker-compose`