# import modules we need
import psycopg2
from update_data import add_respone, add_vsp, check, remove_from_string, delet_from_database

# import our files
from constant import ADMIN_LIST, DBNAME, HOST, PASSWORD, USER
from utilize import if_time_date, make_log

def give(input_name=None, table="Kingdom_Library"):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    # and name_ is not None
    if table == "Kingdom_Library":
        sql = f"select id from {table} where name = \'{input_name}\';"

    elif table == "Kingdom_Library_respone":
        sql = f"select respone from {table} where name = \'{input_name}\';"

    cr.execute(sql)
    respone = cr.fetchall()

    if respone:
        respone = respone[0][0]
        cr.close()

        return respone

    return False


def check(user_input, table_="Kingdom_Library", auto=True):
    type = "media"
    index = 1
    out_index = 0
    if table_ == "Kingdom_Library_respone":
        type = "respone"
        index = 0
        out_index = 1

    result_respone = give(user_input, table_)
    if result_respone:
        return result_respone, type

    else:
        DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
        cr = DB.cursor()
        cr.execute(f"select * from {table_}")
        result = cr.fetchall()
        if user_input is None:
            cr.close()
            return result
        else:
            found = None
            for media in result:
                if media[index] in user_input and len(media[index]) > 2:  # .split in?
                    found = media
                elif media[index] in user_input.split():
                    found = media
            if found:
                return found[out_index], type
            if auto:
                return check(user_input, table_="Kingdom_Library_respone", auto=False)

            return False, False


def return_all():
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    cr.execute(f"select * from Kingdom_Library ")
    result = cr.fetchall()
    returned = []
    for vsp in result:
        returned.append(vsp[0])
    cr.close()
    return returned


def handle_responses(input_massage, chat_id, message_id):
    userinput = str(input_massage).lower()
    # check if respone from admin
    if chat_id in ADMIN_LIST:
        # check if we need to add respone to database
        if 'addrespone ' in userinput or 'addresponellink ' in userinput:
            # split to name respone and add to our respone table
            userinput = remove_from_string(userinput, 'addrespone ')
            if userinput[:4] == 'link':
                userinput = remove_from_string(userinput, 'link ')
                key, value = userinput.split(",")
            else:
                key, value = userinput.split(":")
            add_respone(key, value)

            return (f"the response {userinput} inserted", True)

        # check if we need to remove drom database
        elif 'removerespone ' in userinput:
            userinput = remove_from_string(userinput, 'removerespone ')
            delet_from_database(userinput, "Kingdom_Library_respone")

            return (f"the response {userinput} removed", True)

        # check if we need to add media to database
        elif 'addvoices ' in userinput or 'addstickers ' in userinput or 'addpictures ' in userinput:
            if 'addvoices ' in userinput:
                userinput = add_vsp(userinput, message_id, 'voices')
            elif 'addstickers ' in userinput:
                userinput = add_vsp(userinput, message_id, 'stickers')
            elif 'addpictures ' in userinput:
                userinput = add_vsp(userinput, message_id, 'pictures')

            return (f"{userinput} added succesfully", True)

        # check if we need to remove media from database
        elif 'removesaive ' in userinput or 'removerespo ' in userinput:
            table = "Kingdom_Library"
            if 'removerespo ' in userinput:
                table = "Kingdom_Library_respone"
            userinput = remove_from_string(userinput, 'removesaive ')
            delet_from_database(userinput, table)

            return (f"{userinput} removed succesfully", True)

        # check return a tuple of respone and it's type 
        respone_ = check(userinput)
        respone_ = if_time_date(respone_[0]), "date_time"

        return respone_
