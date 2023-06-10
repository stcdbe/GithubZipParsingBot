import os
from dotenv import load_dotenv

load_dotenv()

APITOKEN = str(os.getenv("API_TOKEN"))

REDISHOST = str(os.getenv('REDISHOST'))
REDISPORT = int(os.getenv('REDISPORT'))
REDISDB = int(os.getenv('REDISDB'))
