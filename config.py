#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋𝙷𝚎𝚕𝚕𝚘 {first}\n\n𝚃𝚑𝚒𝚜 𝚒𝚜 𝚊 𝚂𝚙𝚎𝚌𝚒𝚊𝚕 𝙻𝚒𝚗𝚔 𝙶𝚎𝚗𝚎𝚛𝚊𝚝𝚘𝚛 𝚍𝚎𝚜𝚒𝚐𝚗𝚎𝚍 𝚝𝚘 𝚍𝚎𝚕𝚒𝚟𝚎𝚛 𝚝𝚑𝚎 𝙻𝚊𝚝𝚎𝚜𝚝 𝙼𝚘𝚟𝚒𝚎𝚜, 𝚆𝚎𝚋 𝚂𝚎𝚛𝚒𝚎𝚜, 𝚊𝚗𝚍 𝚖𝚘𝚛𝚎 𝚍𝚒𝚛𝚎𝚌𝚝𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛𝚜 𝚊𝚜 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚏𝚒𝚕𝚎𝚜.\n\n\n𝙹𝚘𝚒𝚗 : @FilmsofFortune 𝚏𝚘𝚛 𝚞𝚙𝚍𝚊𝚝𝚎𝚜!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝙷𝚎𝚢 {first}\n\n<b>𝙿𝚕𝚎𝚊𝚜𝚎 𝚓𝚘𝚒𝚗 𝚖𝚢 𝚞𝚙𝚍𝚊𝚝𝚎𝚜 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 𝚒𝚗 𝚘𝚛𝚍𝚎𝚛 𝚝𝚘 𝚞𝚜𝚎 𝚖𝚎.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "⚡<b>File uploaded by [Films of Fortune](https://t.me/FilmsofFortune)</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{filename}</i>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝚍𝚘 𝚗𝚘𝚝 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝚍𝚒𝚛𝚎𝚌𝚝𝚕𝚢. 𝙹𝚘𝚒𝚗 : @FilmsofFortune 𝚝𝚘 𝚐𝚊𝚒𝚗 𝚊𝚌𝚌𝚎𝚜𝚜 𝚝𝚘 𝚜𝚙𝚎𝚌𝚒𝚊𝚕 𝚕𝚒𝚗𝚔𝚜!"

ADMINS.append(OWNER_ID)
ADMINS.append(5715864408)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
