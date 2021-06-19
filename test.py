# from constant import add_response

# add_response({"هلا":"لاهل"})
# from constant import admin_list

# userinput='هلوو'

# from responses import check_dict
#  

# admin_add_list =list (admin_list)
# admin_add_list.remove(-1001323642182)
#  

# import webbrowser
# webbrowser.open(URL)

# import requests
# text="نزلت فورمة الحضور روحوا سجلوا"
# URL=f"https://api.telegram.org/bot1792666018:AAFdMxINeAY06Thw8aR--DGTqgrObpzrono/sendMessage?chat_id\
# =-1001181247577&text={text}"
# r = requests.get(URL)#, auth=('user', 'pass') r.status_code


# from databaseposgrete import add, save_

# from responses import response_dict

# import pickle

# file_name = "user_id.pkl"
# sample_list = [1, 2 , 3]
# open_file = open(file_name, "wb")

# def add_list()

# open_file = open(file_name, "rb")
# loaded_list = pickle.load(open_file)
# open_file.close()

# loaded_list.append(4)
# open_file = open(file_name, "wb")
# pickle.dump(loaded_list, open_file)
# open_file.close()

#  


# for response in response_dict:
#     add(response, response_dict[response])
#     save_()

# from databaseposgrete import *

#  
#  
# del_('الجدول')
# from responses import response_dict
# DB = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
# cr = DB.cursor()
# cr.execute("create table if not exists Kingdom_Library_respone ( name text,respone text,type text)")
# for reponse in response_dict:
#     add(reponse,response_dict,'respone','Kingdom_Library_respone')
# add('hello','Hi','respone','Kingdom_Library_respone')
# give(name_='hello',table='Kingdom_Library_respone')
# DB.commit()
# cr.close()
# DB.close()


# from datetime import datetime
# import pytz # $ pip install pytz
# from geopy import geocoders # $ pip install geopy

# # find timezone given country and subdivision
# g = geocoders.GoogleV3()
# place, (lat, lng) = g.geocode('us/la')
# timezone = g.timezone((lat, lng))

# # parse rfc3339-like format
# utc_dt = datetime.strptime('2014-04-19 03:39:02.000', '%Y-%m-%d %H:%M:%S.%f')

# # convert utc to the given timezone
# dt = timezone.fromutc(utc_dt)
# # -> datetime.datetime(2014, 4, 18, 22, 39, 2,
# #        tzinfo=<DstTzInfo 'America/Chicago' CDT-1 day, 19:00:00 DST>)
# from zoneinfo import ZoneInfo
# from datetime import datetime, timedelta
# import pytz

# # now= datetime.now()
# # dt = datetime(now, tz=ZoneInfo("America/Los_Angeles"))
# # print(dt)

# utcmoment_naive = datetime.now()
# utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
# localDatetime = utcmoment.astimezone(pytz.timezone('Etc/GMT'))
# print(localDatetime.strftime('%H:%M:%S'))
# print(pytz.all_timezones)

# from responses import if_time_date
# print(if_time_date('time'))
# print(if_time_date('date'))

# If you have local image path:
# from telegram.ext import *
#
# # from main import API_KEY
#
# path="C:\\Users\GLOBAL-PC\Pictures\photo_2021-06-18_23-45-46.jpg"
# API_KEY="1792666018:AAFdMxINeAY06Thw8aR--DGTqgrObpzrono"
# updater = Updater(API_KEY)
# def sendmessag(update,contax):
#     contax.bot.send_photo(-1001181247577, photo=open(path, 'rb'))
# sendmessag(updater)
#     dp = updater.dispatcher
#     dp.add_handler(MessageHandler(Filters.text, sendmessag))
#     updater.start_polling()
#     updater.idle()

# If you have url of image from internet:
# bot.send_photo(chat_id, 'your URl')



