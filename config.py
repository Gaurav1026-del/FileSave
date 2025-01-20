import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "27705761"))
API_HASH = os.environ.get("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")


OWNER_ID = int(os.environ.get("OWNER_ID", "6987158459"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://akashrabha2005:781120@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002216807478"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002392114612"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002426798039"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002337221005"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002247208520"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6987158459]
    for x in (os.environ.get("ADMINS", "6987158459").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ {mention}"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}, 𝖳𝗁𝖺𝗇𝗄𝗌 𝖿𝗈𝗋 𝗎𝗌𝗂𝗇𝗀 𝗆𝖾. 𝖫𝗈𝗏𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 &\n 𝖲𝖾𝗋𝗂𝖾𝗌? 𝖨'𝗆 𝗆𝖺𝖽𝖾 𝗍𝗈 𝗁𝖾𝗅𝗉 𝗐𝖺𝗍𝖼𝗁 𝗐𝗁𝖺𝗍 𝗒𝗈𝗎'𝗋𝖾 𝗅𝗈𝗈𝗄𝗂𝗇𝗀 𝖿𝗈𝗋.\n\n𝖢𝗁𝖾𝖼𝗄 𝗈𝗎𝗍 𝗈𝗎𝗋 𝖼𝗁𝖺𝗇𝗇𝖾𝗅𝗌 𝖻𝖾𝗅𝗈𝗐 𝖿𝗈𝗋 𝗆𝗈𝗋𝖾!👇..")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>›› ʜᴇʏ {mention} × \n\n    ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs.</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6987158459)

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
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
