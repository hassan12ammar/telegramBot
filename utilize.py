# import modules we need
from asyncio.log import logger
from datetime import datetime
import requests
import pytz

# import our files
from constant import SEND_URL



def join_with_sep(list_input, seperator = " , "):
    output_list = seperator.join(list_input)
    return output_list


def send_message(msg, chat_id):
    url = SEND_URL.replace('chat_id', str(chat_id))
    url = url.replace('msg', str(msg))
    url = url.replace(str(chat_id), 'chat_id', 1)

    r = requests.get(url)


def if_time_date(response):
    now = datetime.now(pytz.timezone('Asia/Baghdad'))
    if response[0] == 'time':
        time = now.strftime('%I:%M:%S')  # ("%H:%M:%S")
        response[0] = time
    elif response == 'date':
        date = now.strftime("%d/%m/%y")
        response[0] = date
    return response


def make_log(log_msg):
    logger.info(log_msg)


def remove_from_string(word, remove):
    """
    remove from the beginning of word based
    on the length of the remove latters
    """
    output_name = ''
    checklist = [remove_index for remove_index in range(len(remove))]
    for i in range(len(word)):
        if i not in checklist:
            output_name = output_name + word[i]
    return output_name
