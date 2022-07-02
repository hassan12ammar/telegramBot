# import modules we need
from commands import Bot_command, error, help_command, list_command, sent_all_command, start_comand
from telegram.ext.utils.types import UD
from telegram.ext import *
import logging

# import our files
from constant import API_KEY, FORWAD_CHENNEL_ID, IMS_GROUP_ID, MANAGEMENT_ID, NOTIFICATION_CHANNEL_ID
from update_data import give, update_notification 
from constant import ADMIN_ID, ADMIN_LIST
from responses import handle_responses
# from responses import respone_added, respone_deleted, VPS_added, VPS_deleted
# from responses import respone_detected, VPS_detected
# from utilize import send_message

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def handel_massage(update, context):

    try:
        text = str(update.message.text).lower()
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        from_channel = False
    except:
        text = str(update.channel_post.text)
        chat_id = update.channel_post.chat_id
        message_id = update.channel_post.message_id
        from_channel = True

    if from_channel:
        if chat_id == FORWAD_CHENNEL_ID:
            context.bot.forward_message(chat_id = IMS_GROUP_ID, from_chat_id = chat_id, message_id = message_id)

        if chat_id == NOTIFICATION_CHANNEL_ID:
            update_notification(message_id)

    else:
        response, type = handle_responses(text, chat_id, message_id)

        if response :
            if type == "media":
                chatFrom_id = MANAGEMENT_ID
                context.bot.forward_message(chat_id = chat_id, from_chat_id = chatFrom_id, message_id = response)
            elif type == True:
                update.message.reply_text(response[0])
            else:
                update.message.reply_text(response)
        # else:
        #     print("False")

        # logger.info(f"after responses {response}")


def main():
    updater = Updater(API_KEY)

    logger.info("start :) ")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_comand) )
    dp.add_handler(CommandHandler('help', help_command) )
    # dp.add_handler(CommandHandler('list', list_command) )
    # dp.add_handler(CommandHandler('dict', dict_sent_command) )
    dp.add_handler(CommandHandler('sentitall', sent_all_command) )
    # dp.add_handler(CommandHandler('responses', responses_command) )
    dp.add_handler(CommandHandler('bot', Bot_command) )
    dp.add_handler(MessageHandler(Filters.text, handel_massage) )
    dp.add_error_handler(error)

    updater.start_polling()
    # updater.start_webhook(
    #     listen = '0.0.0.0',
    #     port = PORT,
    #     url_path = API_KEY,
    #     webhook_url = URL + API_KEY, )
    # updater.idle()


if __name__ == '__main__':
    # print("Hello World")
    # send_message("Hello", ADMIN_ID)
    main()
