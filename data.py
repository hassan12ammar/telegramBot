# import modules we need
import psycopg2

# import our files
from constant import DBNAME, HOST, PASSWORD, USER



def save_(DB=psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)):
    DB.commit()
    DB.close()


def add_non_forwarded(id, name, type_added):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    sql_add_respone = "insert into Kingdom_Library (id, name, type) values (%s, %s, %s)"
    cr.execute(sql_add_respone, (str(id), str(name), str(type_added)))
    cr.close()
    save_(DB)


def add_forwarded(message_id, response, type_added):
    message_id += 2
    add_non_forwarded(message_id, response, type_added)
    return f"send me the message to save it with the name {response} in {message_id} id with type {type_added}"


def delet(name, table="Kingdom_Library"):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    cr.execute(f"""delete from {table} where name = '{name}' """)
    save_(DB)
    cr.close()


def edit(name, updated, new_updated, table='Kingdom_Library'):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    cr.execute(f"""UPDATE kingdom_library
              SET {updated} = '{new_updated}'
              WHERE name = '{name}'; """)
    save_(DB)
    cr.close()


def give(input_name=None, table="Kingdom_Library"):
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    if input_name is None:
        cr.execute(f'SELECT * FROM {table}')
        respone = cr.fetchall()
        cr.close()

        return respone

    cr.execute(f'''SELECT (id, type) 
                FROM {table} 
                WHERE name LIKE '{input_name}' ''')
    respone = cr.fetchall()
    cr.close()
    respone = respone[0][0][1:-1].split(',')

    return respone


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

