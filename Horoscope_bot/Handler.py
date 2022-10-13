from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater


updater = Updater(token='5677270788:AAHKSofh8_Tq-dFPg5Cjk3oYAdxO0rXs1ow')

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)