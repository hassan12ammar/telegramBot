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
    requests.get(url)


def if_time_date(response):
    now = datetime.now(pytz.timezone('Asia/Baghdad'))
    if response == 'time':
        response = now.strftime('%I:%M:%S')  # ("%H:%M:%S")
    elif response == 'date' :
        response = now.strftime("%d/%m/%y")
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


def message_added(message_id, response, type_added):
    return f"send me the message to save it with the name {response} in {message_id} id with type {type_added}"
