# import modules we need
from typing import List
import psycopg2

# import our files
from constant import DBNAME, HOST, PASSWORD, USER
from utilize import message_added



def save_(DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)) -> None:
    DB.commit()
    DB.close()


def add_non_forwarded(id:str, name:str, type_added:str) -> None:
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    sql_add_respone = "insert into Kingdom_Library (id, name, type) values (%s, %s, %s)"
    cr.execute(sql_add_respone, (str(id), str(name), str(type_added)))
    cr.close()
    save_(DB)


def add_forwarded(message_id:int, response:str, type_added:str) -> str:
    message_id += 2
    add_non_forwarded(message_id, response, type_added)
    return message_added(message_id, response, type_added)

def delet(name:str, table:str="Kingdom_Library") -> None:
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    cr.execute(f"""delete from {table} where name = '{name}' """)
    save_(DB)
    cr.close()


def edit(name:str, updated:str, new_updated:str, table:str='Kingdom_Library') -> None:
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()
    cr.execute(f"""UPDATE kingdom_library
              SET {updated} = '{new_updated}'
              WHERE name = '{name}'; """)
    save_(DB)
    cr.close()


def give(input_name:str, table:str="Kingdom_Library") -> List[tuple]:
    DB = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
    cr = DB.cursor()

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
    cr.execute(f"select * from Kingdom_Library")
    result = cr.fetchall()
    cr.close()
    return result

