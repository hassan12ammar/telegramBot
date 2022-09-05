# import modules we need
import os
import ast
from dotenv import load_dotenv

# load environment variables 
load_dotenv()

# database variables
HOST = os.environ.get("host")
DBNAME = os.environ.get("dbname")
USER = os.environ.get("user")
PASSWORD = os.environ.get("password")
PORT = int(os.environ.get('PORT') )

# bot variables
TEST_API_KEY = os.environ.get('TEST_BOT_TOKEN')
API_KEY =  os.environ.get('BOT_TOKEN') # TEST_API_KEY
URL = os.environ.get('URL')

# telegram variables
IMS_GROUP_ID = int(os.environ.get('ims_group_is') )
FORWAD_CHENNEL_ID = int(os.environ.get('forwad_message_id') )
NOTIFICATION_CHANNEL_ID = int(os.environ.get('notification_channel_id') )
ADMIN_ID = int(os.environ.get('admin_id') )
MANAGEMENT_ID = int(os.environ.get('management_id') )
PROFOUND_CABAL_ID = int(os.environ.get('profound_cabal_id') )
PERSONAL_CHANEL_ID = int(os.environ.get('not_important_channel_id') )
FORWAD_MESSAGE_ID = int(os.environ.get('forwad_message_id') )

admin_names = ast.literal_eval(os.environ.get("ADMIN_LIST"))
ADMIN_LIST = [globals()[admin_name] for admin_name in admin_names]

SEND_URL = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id=chat_id&text=msg"

