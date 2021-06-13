# import logging
from telegram.ext import *
import constant as key
import responses as r
from databaseposgrete import add, give, remove_, check, sent

updater = Updater(key.API_key)

# Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)

 

# def error(update, context):
#     """Log Errors caused by Updates."""
     



def join_(listy):
    seperator = " , "
    _list = seperator.join(listy)
    
    return _list


def _sent(update):
    all_list = check(None)
    voice_list = []
    sticker_list = []
    picture_list = []
     
    for message in all_list:
        if message[2] == 'voices':
            voice_list.append(message[1])
        elif message[2] == 'stickers':
            sticker_list.append(message[1])
        elif message[2] == 'pictures':
            picture_list.append(message[1])
    #  
    voice_list = join_(voice_list)
    sticker_list = join_(sticker_list)
    picture_list = join_(picture_list)
    update.message.reply_text("متوفر لدينا الاتي:")
    update.message.reply_text(f"الصوتيات :  \n {voice_list}")
    update.message.reply_text(f"الستكرات :  \n {sticker_list}")
    update.message.reply_text(f"الصور : \n {picture_list}")
    update.message.reply_text("ارسل لي كلمه نفر مع اسم السكلولو التي تريدها وسوف نرسلها لك")


def dict_sent_command(update, contax):
     
    dict_responses = key.read_file()
    for key_ in dict_responses:
        update.message.reply_text(key_)


def Bot_command(update, contax):
    update.message.reply_text("نعم حبيبي الغالي تفضل")


def start_comand(update, contax):
    chat_id = update.message.chat_id
     
    update.message.reply_text(f"مرحبا بكم في بوت 𝗞𝗜𝗡𝗚𝗗𝗢𝗠 𝗟𝗜𝗕𝗥𝗔𝗥𝗬 السكلولية"
                              f" الرجاء الانتباه اذ ان هذا البوت يدار من قبل منظمة مملكة الكلاوات العالميه ادامها "
                              f"الله وابقاها "
                              f" ويحمل الكثير من التسافل وان هدفه الاول والاخير هو الهيمنه على العالم لذا وجب التنبيه ")
    update.message.reply_text("بالرفاه والبنين حبيبي")


def help_command(update, contax):   update.message.reply_text("ههه منورني يا ورده انت شتريدني اساعدك بشنو. ")


def list_command(update, contax):
    chat_id=update.message.chat_id
    if chat_id in key.admin_list:
        _sent(update)
    else:update.message.reply_text(" هذا الامر غير متوفر لديك فقط للسادة العظام اعضاء اللملكة")




def sentitall_command(update, context):
    chat_id=update.message.chat_id
    if chat_id in key.admin_list:
        all_ = sent()
         
        for voice in all_:
             
            chatIDfor = update.message.chat_id
            chatID = -1001229538530
            name_=give(voice)[1]
            type_=give(voice)[2]
            update.message.reply_text(f"{name_} , {type_}")
            context.bot.forward_message(chat_id=chatIDfor, from_chat_id=chatID, message_id=voice)
    else: update.message.reply_text("شنو انت لوتي لو تستلوت علينه هذا الامر بس للادمنيه")


def responses_command(update,contax):
    key_, valu_ = key.read_file()
    #  
    return key_,valu_
    # update.message.reply_text(valu_)


def addy(response, update, type):
     
    name_ = remove_(response, f'add{type} ')
    id_ = update.message.message_id + 2
     
    add(id_, name_, type)
    update.message.reply_text(f"send me the message to save it with the name {name_} in {id_} id with type {type}")


def handel_massage(update, context):
        print("hello msg")
    # try:
        text = str(update.message.text).lower()
        chat_id = update.message.chat_id
        response = r.sample_responses(text, chat_id)
        if type(response) is int:
            chatFrom_id = -1001229538530
            context.bot.forward_message(chat_id=chat_id, from_chat_id=chatFrom_id, message_id=response)
             
        if 'addvoices ' in response:
             
            addy(response, update, 'voices')
        elif 'addstickers ' in response:
            addy(response, update, 'stickers')
        elif 'addpictures ' in response:
            addy(response, update, 'pictures')

        elif response == 'Done!':
            id_ = update.message.message_id - 1
            name_ = give(id_)[1]
            update.message.reply_text(f"{response} name is {name_} in {id_} id")
        elif response == 'remove':
            update.message.reply_text("okay I removed it.")
        else :
             
            update.message.reply_text(response)
    # except error() as e:
        # update.message.reply_text("something goes wrong!!")
         


# def error(updater, contax): logging.error(f"error{updater} causees error {contax.error}")


def main():
    print("hello starting")
    global updater
    dp = updater.dispatcher
     

    dp.add_handler(CommandHandler('start', start_comand))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('list', list_command))
    dp.add_handler(CommandHandler('dict', dict_sent_command))
    dp.add_handler(CommandHandler('sentitall', sentitall_command))
    dp.add_handler(CommandHandler('responses', responses_command))
    dp.add_handler(CommandHandler('bot', Bot_command))
    dp.add_handler(MessageHandler(Filters.text, handel_massage))
    # dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()



main()
