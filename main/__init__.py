#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("15740669", default=None, cast=int)
API_HASH = config("ca407b33953bcdba283fc3b81c19d059", default=None)
BOT_TOKEN = config("5808384079:AAG8mLXrXUO0IXMdVIi6LkqEtxigEUB27Rs", default=None)
SESSION = config("BQCbmnw4E9qjXT6tXhBatDPdXj48kkM0OMWa_v2b8PLwuykGwRFLKRVIca0PL7VLGxbAEhZYz2jfPC9BrMfyTFPjLgpjo1nHYNRiMqOEgbjdkKN59szS3zwzTm_UjWIvL6GPf88QAcHvr3RKa774eUBrCiO1pTgIOrQlltrjfCCPxadF8K73u9uND6WIR9W0UqzqcvmnqsQPPxrdIaJEcr6fn1kAhyMlr-_l3PSjn6VB9dneU_WQO0DDMbSp417z_81uZ_-GA4rg_rl3H2c7M_OXY2TZ0-anb7mss1F7m05yfpTTVMtkEjWguCFYADeN9fs-YxCXwwrNxmBpzH7VedCtRihRYAA", default=None)
FORCESUB = config("rclone5bot", default=None)
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
