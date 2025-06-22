import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8001511132:AAF-5YYbyjKc8qGtt5h6q4m4fC0shbXqTp8")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25649636"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "43af470d1c625e603733268b3c2f7b8f")

# String Session (still left blank as per previous setup)
SESSION = os.environ.get("SESSION", "BQFziNcAb6er2cHfW4tzBwQ-vg6hOQYCaNqZ17secmVBCJGhFqZFGRKuiHF2Fbds67zwTkBDn6Ljwyn0F6uhvd30wWqQpFUKmR5upyWiTeuO-XBu4h8sISMu97dV67BwBBxFXaU2pEoEyd9B0zXF8P9ofdkEdj9jpj73syt5eX4fjypq_l0soEoY9fgbqFflxshAtZ8u8kMYwfTqptHgZOa1kDwF2bDaIanDk4Vpm1ggkHOfzDW4YyS76VF7Q4sbqljqaXpRS5jVY0K46OEaxHdTq0aNBPKemNsXqZkLUET73jDlCMqjQVxYyLsZ8IJ46_xNokC_uDXq-ViZ-q4NIjop6BjmhAAAAAGmjQMiAA")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7815236348"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get(
    "DB_URI", 
    "mongodb+srv://Goku_bhai001:iS5sYySFKS2xZZpc@cluster0.voj0eyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = os.environ.get("DB_NAME", "scrapper2")

FILE_CHANNEL = int(os.environ.get("FILE_CHANNEL", "-1002329960018"))
FILE_BOT_USERNAME = os.environ.get("FILE_BOT_USERNAME", "oxytocinlinksbot")

BYPASS = bool(os.environ.get("BYPASS", False))
BYPASS_BOT_USERNAME = os.environ.get("BYPASS_BOT_USERNAME", "FERITURLBOT")

# How to watch video guide link
HOW_TO_WATCH_LINK = os.environ.get("HOW_TO_WATCH_LINK", "https://t.me/how_bot_work/7")
