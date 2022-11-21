import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5772038344:AAEcIiMZQOpx4h17sf3KLJ16KUyXXQmCpj4")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "15532790"))
    API_HASH = os.environ.get("API_HASH", "52c9ce174794ba4c750f71978c8dfa65")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://publicdatabase:2EzVBS74xlPzXkTn@cluster0.0ujkh.mongodb.net/?retryWrites=true&w=majority")
    
