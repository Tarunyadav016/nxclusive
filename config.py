import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8001511132:AAFnHdzYwmjswrmxLgfT8K08dgztilmNUx0")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25649636"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "43af470d1c625e603733268b3c2f7b8f")

# String Session (still left blank as per previous setup)
SESSION = os.environ.get("SESSION", "BQFziNcAbMsqpI10Yw2wcBVejCsyneKywuojfuywbIIH6x1apu8DUokswbzCTqU5NEixIO15pe2hotyrvrA_PD7w9S38WTp8aFRG1yepGNjmDRakjF8pXFXl-oZvoOrF_AIr5PAnFEBymu30y881kSYA-H-IN2TXXDC_RsIRXWTVgvLr8IMusEW98_Af0epC9yf1uIH_Q0VQWesdbhyajBFYENh4qJu0gInSdvp6HUguerjcARMpD6GLNwJdM7KFfItVwhD0HuF8SBJM_Gif78xkxarkIs8ayog9Mnp5-OJVa-plzlW4FrbuJrM4nay7c99MYsxJrUBBvlyVi4IPaU_DBC_enQAAAAGmjQMiAA")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7815236348"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get(
    "DB_URI", 
    "mongodb+srv://Goku_bhai001:iS5sYySFKS2xZZpc@cluster0.voj0eyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = os.environ.get("DB_NAME", "scrapper2")

FILE_CHANNEL = int(os.environ.get("FILE_CHANNEL", "-1002449127698"))
FILE_BOT_USERNAME = os.environ.get("FILE_BOT_USERNAME", "Xclusivehub_bot")

BYPASS = bool(os.environ.get("BYPASS", False))
BYPASS_BOT_USERNAME = os.environ.get("BYPASS_BOT_USERNAME", "Nick_Bypass_Bot")

# How to watch video guide link
HOW_TO_WATCH_LINK = os.environ.get("HOW_TO_WATCH_LINK", "https://t.me/how_bot_work/7")

