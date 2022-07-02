# import modules we need
from asyncio.log import logger
from datetime import datetime
import requests
import logging
import json
import pytz

# import our files
from constant import SEND_URL


def join_with_sep(list_input, seperator = " , "):
    output_list = seperator.join(list_input)
    return output_list

def send_message(msg, chat_id):
    url = SEND_URL.replace('chat_id', chat_id)
    url = url.replace('msg', msg)
    url = url.replace(chat_id, 'chat_id', 1)

    r = requests.get(url)

def if_time_date(response):
    now = datetime.now(pytz.timezone('Asia/Baghdad'))
    if response == 'time':
        time = now.strftime('%I:%M:%S')  # ("%H:%M:%S")
        response = time
    elif response == 'date':
        date = now.strftime("%d/%m/%y")
        response = date
    # logger.info(f"time date return {response}")
    return response

def read_file():
    with open('responses.json', encoding="utf8") as f:
        data = f.read()
    response_dict = json.loads(data, strict=False)
    f.close()
    return dict(response_dict)

def update_file(new_dict):
    with open('responses.json', 'r+', encoding="utf8") as file:
        file.seek(0)
        json.dump(new_dict, file, indent=4, ensure_ascii=False)
        file.truncate()
    return f"the response {new_dict} added"
# Enable logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

def make_log(log_msg):
    logger.info(log_msg)


def remove_from_string(word, remove):
    output_name = ''
    checklist_ = []
    for remove_index in range(len(remove)):
        checklist_.append(remove_index)
    for i in range(len(word)):
        if i not in checklist_:
            output_name = output_name + word[i]
    return output_name
