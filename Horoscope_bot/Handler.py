from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
import requests


updater = Updater(token='5677270788:AAHKSofh8_Tq-dFPg5Cjk3oYAdxO0rXs1ow')

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def signRequest(update: Update, context: CallbackContext):
    params = (
        ('sign', update.message.text),
        ('day', 'today')
    )
    response = requests.post('https://aztro.sameerkumar.website/', params=params)
    jsonResponse = response.json()


    context.bot.send_message(chat_id=update.effective_chat.id, text = jsonResponse["description"])

echo_handler = MessageHandler(Filters.text & (~Filters.command), signRequest)
dispatcher.add_handler(echo_handler)