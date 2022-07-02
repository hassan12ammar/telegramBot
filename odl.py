"""
def remove_response(remove_response):
    with open('responses.json', 'r+', encoding="utf8") as file:
        file_data = json.load(file)
        if remove_response in file_data:
            file_data.pop(remove_response)
            file.seek(0)
            json.dump(file_data, file, indent=4)
            return_ = "the response added"
        else:
            return None

def add_to_list(msg_id):
    file = "report_id.pkl"
    list_file = open(file, "rb")
    loaded_list = pickle.load(list_file)
    for i in range(len(loaded_list) - 1, 0, -1):
        loaded_list[i] = loaded_list[i - 1]
    loaded_list[0] = msg_id
    list_file.close()
    list_file_ = open(file, "wb")
    pickle.dump(loaded_list, list_file_)
    list_file_.close()
    return loaded_list

def get_from_list(num):
    file = "report_id.pkl"
    list_file = open(file, "rb")
    loaded_list = pickle.load(list_file)
    list_file.close
    return loaded_list[num-1]

cr.execute("create table if not exists Kingdom_Library (id integer , name text,type text)")
cr.execute("create table if not exists Kingdom_Library_respone (name text, respone text)")

        elif 'اخر تبليغ' in response :
            try:
                if response == 'اخر تبليغ':
                    last_notification_command(update, context,1)
                elif response == 'قبل اخر تبليغ':
                    last_notification_command(update, context,2)
                elif response == 'قبل قبل اخر تبليغ':
                    last_notification_command(update, context,3)
            except:
                pass

        elif 'addvoices ' in response:
            add_vsp(response, update, 'voices')
        elif 'addstickers ' in response:
            add_vsp(response, update, 'stickers')
        elif 'addpictures ' in response:
            add_vsp(response, update, 'pictures')

        elif response == 'Done!':
            id_ = update.message.message_id - 1
            name_ = give(id_)[1]
            update.message.reply_text(f"{response} name is {name_} in {id_} id")
        elif response == 'remove':
            update.message.reply_text("okay I removed it.")
        else:
            logger.info("reply from else")
            update.message.reply_text(response)

def last_notification_command(update, context, pos = 1):
    chat_id = update.message.chat_id
    chatFrom_id = notification_channel_id 
    message_id = key.get_from_list(pos)
    context.bot.forward_message(chat_id = chat_id, from_chat_id = chatFrom_id, message_id = message_id)  # 288

def dict_sent_command(update, contax):
    dict_responses = key.read_file()
    for key_ in dict_responses:
        update.message.reply_text(key_)

dp.add_handler(CommandHandler('last_report', last_notification_command) )


def add_respone(name, respone):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    sql_add_respone = "insert into Kingdom_Library_respone (name, respone) values (%s, %s)"
    cr.execute(sql_add_respone, (name, respone))
    save_(DB)
    cr.close()

'''

"""
'''
def update_notification(new_id):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()

    notification_list = ["thr_befor_last", "tow_befor_last", "one_befor_last", "last"]

    for column in range(len(notification_list) - 1):
        current_notification = notification_list[column]
        after_notification = notification_list[column + 1]

        cr.execute(f""" UPDATE Kingdom_Library SET
                        id = (select id from Kingdom_Library where name = '{after_notification}')
                        WHERE name = '{current_notification}' AND type = 'notification'; """)
        # print(column)
    cr.execute(f""" UPDATE Kingdom_Library SET
                    id = {new_id}
                    WHERE name = '{notification_list[-1]}' AND type = 'notification'; """)
    # print(len(notification_list) - 1)

    # DB.commit()
    save_(DB)

    # print("Done")
    cr.close()

'''