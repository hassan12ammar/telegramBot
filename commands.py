# import modules we need
from logging import Logger

# import our files
from constant import ADMIN_LIST, MANAGEMENT_ID
from responses import give, return_all
from utilize import join_with_sep, make_log
from update_data import check


def Bot_command(update, contax):
    update.message.reply_text("نعم حبيبي الغالي تفضل")


def start_comand(update, contax):
    update.message.reply_text(f"مرحبا بكم في بوت 𝗞𝗜𝗡𝗚𝗗𝗢𝗠 𝗟𝗜𝗕𝗥𝗔𝗥𝗬 السكلولية"
                              f" الرجاء الانتباه اذ ان هذا البوت يدار من قبل منظمة مملكة الكلاوات العالميه ادامها "
                              f"الله وابقاها "
                              f" ويحمل الكثير من التسافل وان هدفه الاول والاخير هو الهيمنه على العالم لذا وجب التنبيه ")
    update.message.reply_text("بالرفاه والبنين حبيبي")


def help_command(update, contax):   
    update.message.reply_text("ههه منورني يا ورده انت شتريدني اساعدك بشنو. ")

def error(update, context):
    """ Log Errors caused by Updates. """
    Logger.warning('Update "%s" caused error "%s"', update, context.error)


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
    voice_list = join_with_sep(voice_list)
    sticker_list = join_with_sep(sticker_list)
    picture_list = join_with_sep(picture_list)
    update.message.reply_text("متوفر لدينا الاتي:")
    update.message.reply_text(f"الصوتيات :  \n {voice_list}")
    update.message.reply_text(f"الستكرات :  \n {sticker_list}")
    update.message.reply_text(f"الصور : \n {picture_list}")
    update.message.reply_text("ارسل لي كلمه نفر مع اسم السكلولو التي تريدها وسوف نرسلها لك")

def list_command(update, contax):
    # logger.info(" from list ")
    chat_id = update.message.chat_id
    if chat_id in ADMIN_LIST:
        # logger.info(" from list admin ")
        _sent(update)
    else:
        make_log(" from list not admin")
        update.message.reply_text(" هذا الامر غير متوفر لديك فقط للسادة العظام اعضاء اللملكة")

def sent_all_command(update, context):
    chat_id = update.message.chat_id
    if chat_id in ADMIN_LIST:
        all_ = return_all()

        for voice in all_:
            chatIDfor = update.message.chat_id
            chatID = MANAGEMENT_ID
            returned_give = give(voice)
            name_ = returned_give[1]
            type_ = returned_give[2]
            update.message.reply_text(f"{name_} , {type_}")
            context.bot.forward_message(chat_id=chatIDfor, from_chat_id=chatID, message_id=voice)
    else:
        update.message.reply_text("شنو انت لوتي لو تستلوت علينه هذا الامر بس للادمنيه")
