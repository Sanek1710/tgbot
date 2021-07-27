import dotenv
dotenv.load_dotenv()
import os
from logger import LOG

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler
from telegram.ext.filters import Filters
import requests


MY_CHAT_ID = int(os.getenv('MY_CHAT_ID', 0))
TELEGRAM_BOT_ID = os.getenv('TELEGRAM_BOT_ID', '')

GET_IP_URL = 'https://api.ipify.org'
ADMINS = [MY_CHAT_ID]

def ip(bot, update):
    chat_id = update.message.chat_id
    LOG.info("ip request: %s", chat_id)
    if chat_id in ADMINS:
        # bot.send_photo(chat_id=chat_id, photo=url)
        try:
            ip = requests.get(GET_IP_URL).text
            bot.send_message(chat_id=chat_id, text=ip)
        except Exception as e:
            LOG.error(e)
    
def msg_handler(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text

    LOG.info('message from %s: "%s"', chat_id, message)

    if chat_id in ADMINS:
        bot.send_message(chat_id=chat_id, text=message)
    else:
        bot.send_message(chat_id=chat_id, text='Вас нет в списке приглашенных.')
 

def main():
    updater = Updater(TELEGRAM_BOT_ID)
    dp = updater.dispatcher
    dp.bot.send_message(chat_id=MY_CHAT_ID, text='Я запустился!')
    dp.add_handler(CommandHandler('ip', ip))
    dp.add_handler(MessageHandler(Filters.all, msg_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()