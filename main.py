# import modules we need
from commands import Bot_command, error, help_command, list_command, sent_all_command, start_comand
from telegram.ext import *

# import our files
from constant import API_KEY, MANAGEMENT_ID, PORT, URL
from responses import handle_responses


def handel_massage(update, context):
    # get current chat variables
    text = str(update.message.text).lower()
    chat_id = update.message.chat_id
    message_id = update.message.message_id

    # get the appropriate response
    response = handle_responses(text, chat_id, message_id)

    # take the proper action
    if response :
        type_respone = response[-1]
        # check if we need to forward
        if type_respone[-1] == '1':
            chatFrom_id = MANAGEMENT_ID
            context.bot.forward_message(chat_id = chat_id, from_chat_id = chatFrom_id, 
                                        message_id = response[0].strip('"'))
        elif type_respone[-1] == '0':
            update.message.reply_text(response[0].strip('"'))
        elif response[1]=='add' or response[1]=='edit' or response[1]=='remove':
            update.message.reply_text(response[0].strip('"'))

def main():
    updater = Updater(API_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('bot', Bot_command) )
    dp.add_handler(CommandHandler('help', help_command) )
    dp.add_handler(CommandHandler('list', list_command) )
    dp.add_handler(CommandHandler('start', start_comand) )
    dp.add_handler(CommandHandler('sentitall', sent_all_command) )

    dp.add_handler(MessageHandler(Filters.text, handel_massage) )

    dp.add_error_handler(error)

    # updater.start_polling()
    updater.start_webhook(
        listen = '0.0.0.0',
        port = PORT,
        url_path = API_KEY,
        webhook_url = URL + API_KEY, )
    updater.idle()


if __name__ == '__main__':
    main()
