# import our files
from constant import ADMIN_LIST, MANAGEMENT_ID
from utilize import join_with_sep, make_log
from data import return_all


def bot_command(update, contax):
    update.message.reply_text("نعم حبيبي الغالي تفضل")


def start_comand(update, contax):
    update.message.reply_text(f"مرحبا بكم في بوت 𝗞𝗜𝗡𝗚𝗗𝗢𝗠 𝗟𝗜𝗕𝗥𝗔𝗥𝗬 السكلولية"
                              f" الرجاء الانتباه اذ ان هذا البوت يدار من قبل منظمة مملكة العصبة العميقة (سابقا الكلاوات العالميه) ادامها "
                              f"الله وابقاها "
                              f" ويحمل الكثير من التسافل وان هدفه الاول والاخير هو الهيمنه على العالم لذا وجب التنبيه ")
    update.message.reply_text("بالرفاه والبنين حبيبي")


def help_command(update, contax):   
    update.message.reply_text("ههه منورني يا ورده انت شتريدني اساعدك بشنو. ")


def error(update, context):
    """ Log Errors caused by Updates """
    make_log(f'Update "{update}" caused error "{context.error}"')


def send_all(update):
    # get all response in database
    all_list = return_all()

    # declare variables for each type 
    voice_list = []
    sticker_list = []
    picture_list = []
    other_list = []

    # check and assign each respone with its type
    for message in all_list:
        if message[2][:-1] == 'voices':
            voice_list.append(message[1])
        elif message[2][:-1] == 'stickers':
            sticker_list.append(message[1])
        elif message[2][:-1] == 'pictures':
            picture_list.append(message[1])
        else:
            other_list.append(message[1])

    # make lists readable
    voice_list = join_with_sep(voice_list)
    sticker_list = join_with_sep(sticker_list)
    picture_list = join_with_sep(picture_list)
    other_list = join_with_sep(other_list)

    update.message.reply_text("متوفر لدينا الاتي:")
    update.message.reply_text(f"الصوتيات :  \n {voice_list}")
    update.message.reply_text(f"الستكرات :  \n {sticker_list}")
    update.message.reply_text(f"الصور : \n {picture_list}")
    update.message.reply_text(f"الاخرى : \n {other_list}")
    update.message.reply_text("ارسل لي كلمه نفر مع اسم السكلولو التي تريدها وسوف نرسلها لك")


def list_command(update, contax):
    chat_id = update.message.chat_id
    if chat_id in ADMIN_LIST:
        send_all(update)
    else:
        update.message.reply_text(" هذا الامر غير متوفر لديك فقط للسادة العظام اعضاء اللملكة")

