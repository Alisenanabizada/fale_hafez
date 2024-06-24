import logging
import requests
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, CallbackContext
from uuid import uuid4
from dotenv import load_dotenv
import os

load_dotenv("./.env")

token = os.getenv("Token")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handler. This usually takes the two arguments update and context.
def start(update: Update, context: CallbackContext) -> None:
    # Send a message when the command /start is issued.
    update.message.reply_text('/fal نیت نموده روی کلیک کنید.')

def fal(update: Update, context: CallbackContext) -> None:
    # Fetch a random fal from the Flask app
    response = requests.get('http://localhost:9999/fal')
    data = response.json()
    update.message.reply_text(f"{data['ghazal']}\n\n{data['fal']}")

def inline_fal(update: Update, context: CallbackContext) -> None:
    query = update.inline_query.query
    if query == "":
        return

    # Fetch a random fal from the Flask app
    response = requests.get('http://localhost:9999/fal')
    data = response.json()
    ghazal = data['ghazal']
    fal = data['fal']

    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Get a fal",
            input_message_content=InputTextMessageContent(f"{ghazal}\n\n{fal}")
        )
    ]

    update.inline_query.answer(results)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("fal", fal))

    # Handle inline queries
    dispatcher.add_handler(InlineQueryHandler(inline_fal))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()
