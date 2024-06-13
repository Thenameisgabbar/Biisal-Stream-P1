# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "Fɪʟᴇ𝟸Sᴛʀᴇᴀᴍ Rᴏʙᴏᴛ"
bisal_channel = "https://telegram.me/MoviesHubFree4You"
bisal_grp = "https://t.me/+9NJBWRn9BLliNjcy"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '17257388'))
    API_HASH = str(getenv('API_HASH', '3da6517a9fb9840d1867a6712a231872'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '7085813584:AAHamIUKSIZcyBJsvvwXMBuq79YMJ4BDFPY'))
    name = str(getenv('name', 'File2Stream_Robot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002127703761'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1002053387203'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = [int(x) for x in os.environ.get("OWNER_ID", "763351261").split()]
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'DOCTORx98'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://biisal-file-stream.onrender.com/".format(FQDN)
    else:
        URL = "http://biisal-file-stream.onrender.com/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Premium2099:Ashish2099@premium.ovoreus.mongodb.net/?retryWrites=true&w=majority&appName=Premium'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'MoviesHubFree4You')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002053387203")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1002053387203")).split()))   
    BAN_ALERT = str(getenv('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.Pʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ @biisal_bot ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>'))
