#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("2666511", default=None, cast=int)
API_HASH = config("5135858a03edc1f0bac8a6dc8556f08d", default=None)
BOT_TOKEN = config("5878216369:AAF9VR588GcVoKCcFHum8K_fxkRegg7bwFU", default=None)
SESSION = config("BQALIYkXxiKQvhq9wgCUCkqMuZlAWrZ0Z2FfC9ZaIDeYyvNXKTiyQax7etFHnasL6XS2iV4spqQjT8xYYFH3-_oe0gJPuVW-OmR1j9jbuGJ_LIYZj3IgfalZkjHc2JfXRKOscPj3JmkcFSnJzszngqqn0-tdT0vAA2DWiiqYj076nUYfdxLE5l_sRtx0AMPcdEjJFSgbH1WSDKJlfxeMS4wd_RZrkEbkyaaoy4uyDy5B7R8sswFY_DpWJvFXMWTaF-ATdLXBpcDuaNrECbDamhdAcRq_QsVg2vw1fRY59QxKJuiT6hlP34Z-DJTMwVdEKnU4y-imPyP7ZYaRvMaXkQWUW7B1tQA", default=None)
FORCESUB = config("saveown_bot", default=None)
AUTH = config("1538291125", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
