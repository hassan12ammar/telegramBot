import psycopg2

host = 'ec2-34-193-113-223.compute-1.amazonaws.com'
dbname = 'd7nrin8sqh6gp'
user = 'byucljmvrtfrto'
password = '519adea1e37f08cfe2b8f391f9697785ba75b3240373024c71cf037a53e8e3e4'

DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
cr = DB.cursor()


# cr.execute("create table if not exists Kingdom_Library (id integer , name text,type text)")


def save_(DB= psycopg2.connect(host=host, dbname=dbname, user=user, password=password)):
    DB.commit()


def add(id_, name_, type):
    DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    cr = DB.cursor()
    cr.execute(f"insert into Kingdom_Library (id , name,type) values ({id_}, '{name_}','{type}')")
    cr.close()
    save_(DB)


def addrespone(name,respone):
    DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    cr = DB.cursor()
    cr.execute(f"insert into Kingdom_Library_respone (name,respone) values ('{name}','{respone}')")
    cr.close()
    save_(DB)


def del_(name_):
    DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    cr = DB.cursor()
    cr.execute(f"delete from Kingdom_Library where name ='{name_}'")
    save_(DB)
    cr.close()
    return "okay I removed it."


def give(id_=None, name_=None):
    DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    cr = DB.cursor()
    result = None
    if id_ is not None:
        cr.execute(f"select * from Kingdom_Library where id={id_}")
        result = cr.fetchall()[0:3]
    elif name_ is not None:
        cr.execute(f"select * from Kingdom_Library where name='{name_}'")
        result = cr.fetchall()[0:3]
        # [].__len__
    if len(result)==0 :
         result = 'not'
    cr.close()
    return result[0]


def check(name_):
    name_result_ = give(name_=name_)
    if name_result_ != 'n':
        return name_result_[0]
    else:
        DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cr = DB.cursor()
        cr.execute(f"select * from Kingdom_Library ")
        result = cr.fetchall()
        if name_ is None:
            cr.close()
            return result
        else:
            found = None
            for voice in result:
                if voice[1] == name_:
                    found = voice
                elif voice[1] in name_ and len(voice[1]) > 2:  # .split in?
                    found = voice
                elif voice[1] in name_.split():
                    found = voice
            if found is not None: return found[0]        
            return "منورني يا ورده انت ماعدنه هيج كلاوات اختار صوتيه موجوده بعد كلبي"


def remove_(word, remove):
    name__ = ''
    checklist_ = []
    for num in range(len(remove)):
        checklist_.append(num)
    for i in range(len(word)):
        if i not in checklist_:
            name__ = name__ + word[i]
    return name__


def sent():
    DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    cr=DB.cursor()
    cr.execute(f"select * from Kingdom_Library ")
    result = cr.fetchall()
    result_ = []
    for voice in result:
        result_.append(voice[0])      
    cr.close()
    return result_

cr.close()
DB.close()
