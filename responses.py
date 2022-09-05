# import our files
from constant import ADMIN_LIST
from utilize import if_time_date, remove_from_string, send_message
from data import add_non_forwarded, add_forwarded, delet, edit, give


def handle_responses(input_massage, chat_id, message_id):
    userinput = str(input_massage).lower()
    """addtype0 ...... || addtype1 ... """
    """edittype0 ..... || edittype1 ... """
    """removetype0 ... || removetype1 ... """
    """0 -> non-forward && 1 -> forward"""
    # check if respone from admin
    if chat_id in ADMIN_LIST:
        splited = userinput.split()
        # check if we need to add
        if 'add' in splited[0]:
            type_added =  splited[0]
            # remove add from the type
            type_added = remove_from_string(splited[0], 'add')
            # check waht we need to add forwarded 
            if type_added[-1] == '1':
                respone = add_forwarded(message_id, splited[1], type_added)

            # check waht we need to add non-forwarded 
            elif type_added[-1] == '0':
                text, sep = splited[1], splited[1].index(':')
                key, value = text[:sep], text[sep+1:]

                add_non_forwarded(key, value, type_added)

                respone = f"the response {text} inserted"

            return (respone, 'add')

        elif 'remove' in splited[0]:
            delet(splited[1], "Kingdom_Library")
            return (f"the response {splited[1]} removed", 'remove')

        elif 'edit' in splited[0]:
            edit(splited[1], splited[2], splited[3])
            return (f"the {splited[2]} of response {splited[1]} updated to {splited[3]}", 'edit')

        elif 'send_to' in splited[0]:
            send_message(msg=splited[2], chat_id=splited[1])
            return

        # check return a tuple of respone and it's type
        respone = give(userinput)
        respone[0] = if_time_date(respone[0])

        return respone
