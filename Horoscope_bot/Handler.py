from telegram.ext import MessageHandler, Filters, CommandHandler, CallbackContext, Updater
from telegram import Update, ReplyKeyboardMarkup



updater = Updater(token='5677270788:AAHKSofh8_Tq-dFPg5Cjk3oYAdxO0rXs1ow')
dispatcher = updater.dispatcher

keyboard = [["Aries♈️", "Taurus♉️", "Gemini♊️"],
            ["Cancer♋️", "Leo♌️", "Virgo♍️"],
            ["Libra♎️", "Scorpio♏️", "Sagittarius♐️"],
            ["Capricorn♑️", "Aquarius♒️", "Pisces♓️"]]

reply_markup = ReplyKeyboardMarkup(keyboard)




def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Select a sign!", reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)