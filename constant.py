from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# 
HOST = os.environ.get("host")
DBNAME = os.environ.get("dbname")
USER = os.environ.get("user")
PASSWORD = os.environ.get("password")

# 
API_KEY = os.environ.get('TEST_BOT_TOKEN')
URL = os.environ.get('URL')
PORT = int(os.environ.get('PORT') )
# BOT_TOKEN = os.environ.get('BOT_TOKEN')

# 
IMS_GROUP_ID = int(os.environ.get('ims_group_is') )
FORWAD_CHENNEL_ID = int(os.environ.get('forwad_message_id') )
NOTIFICATION_CHANNEL_ID = int(os.environ.get('notification_channel_id') )
ADMIN_ID = int(os.environ.get('admin_id') )
MANAGEMENT_ID = int(os.environ.get('management_id') )
PROFOUND_CABAL_ID = int(os.environ.get('profound_cabal_id') )
PERSONAL_CHANEL_ID = int(os.environ.get('not_important_channel_id') )
FORWAD_MESSAGE_ID = int(os.environ.get('forwad_message_id') )

ADMIN_LIST = [PROFOUND_CABAL_ID, ADMIN_ID, MANAGEMENT_ID]

SEND_URL = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id=chat_id&text=msg"

