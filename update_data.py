# import modules we need
import psycopg2

# import our files
from constant import DBNAME, HOST, PASSWORD, USER
from utilize import remove_from_string


def save_(DB=psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)):
    DB.commit()


def add(id, name, type):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    sql_add_respone = "insert into Kingdom_Library (id, name, type) values (%s, %s, %s)"
    cr.execute(sql_add_respone, id, name, type)
    cr.close()
    save_(DB)


def delet(name, table="Kingdom_Library"):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    cr.execute(f"""delete from {table} where name = '{name}' """)
    save_(DB)
    cr.close()


def add_vsp(response, type, message_id):
    name = remove_from_string(response, f'add{type} ')
    message_id += 2
    add(message_id, name, type)
    return (f"send me the message to save it with the name {name} in {message_id} id with type {type}")

# cr.close()
# DB.close()
