import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins_id = [
    427138092
]

PG_USER = str(os.getenv('PG_USER'))
PG_PASSWORD = str(os.getenv('PG_PASSWORD'))
ip = str(os.getenv('ip'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{ip}/{DATABASE}'