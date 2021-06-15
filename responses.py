from datetime import datetime

import pytz

from constant import read_file, update_file, admin_list
from databaseposgrete import save_, check, remove_, del_
from main import logger

response_dict = read_file()


def if_time_date(response):
    utcmoment_naive = datetime.now()
    utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
    now = utcmoment.astimezone(pytz.timezone('Etc/GMT'))
    # now = datetime.now()
    time = now.strftime('%I:%M:%S')  # ("%H:%M:%S")
    date = now.strftime("%d/%m/%y")
    if response == 'time':
        response = time
    if response == 'date':
        response = date
    logger.info(f"time date return {response}")
    return response


def check_dict(message):
    if message in response_dict:
        response = response_dict[message]
        response = if_time_date(response)
        return response
    for key in response_dict:
        if key in message:
            response = response_dict[key]
            response = if_time_date(response)
            return response
    return None


def sample_responses(input_massage, chat_id):
    userinput = str(input_massage.lower())
    admin_add_list = list(admin_list)
    admin_add_list.remove(-1001323642182)
    if chat_id in admin_add_list:  # ==496530156 or chat_id == -1001229538530:

        if 'addrespone ' in userinput or 'addresponellink ' in userinput:
            #  
            userinput = remove_(userinput, 'addrespone ')
            if userinput[:4] == 'link':
                userinput = remove_(userinput, 'link ')
                key, value = userinput.split(",")
            else:
                key, value = userinput.split(":")
            response_dict[key] = value
            update_file(response_dict)

            return f"the response {userinput} inserted"
        elif 'removerespone ' in userinput:

            userinput = remove_(userinput, 'removerespone ')
            del response_dict[userinput]
            if len(response_dict) == 0:
                update_file(response_dict)

            return f"the response {userinput} removed"

        elif 'addvoices ' in userinput or 'addstickers ' in userinput or 'addpictures ' in userinput:

            return userinput

        elif userinput == 'save':
            save_(); return 'Done!'

        elif 'removesaive ' in userinput:
            userinput = remove_(userinput, 'removesaive ')

            del_(userinput)
            #  
            return "remove"

    if 'نفر ' in userinput:
        #  
        userinput_ = remove_(userinput, 'نفر ')
        message_id = check(userinput_)

        if message_id == 'didnt work': return 'منورني ياوردة انت ماكو هيج كلاوات عدنه'
        return message_id

    else:
        #  
        message_id = check(userinput)

        if type(message_id) is int:
            return message_id
        check_dict_ = check_dict(userinput)
        if check_dict_ is not None:
            return check_dict_

        # else:
        # return userinput
