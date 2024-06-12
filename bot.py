import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Load environment variables from .env file
load_dotenv()

# Read environment variables
TOKEN = os.getenv('TOKEN')
PASSWORD = os.getenv('PASSWORD')
PASTEBIN_ID = os.getenv('PASTEBIN_ID')
PASTEBIN_PASSWORD = os.getenv('PASTEBIN_PASSWORD')
FLAG = os.getenv('FLAG')

def start(update: Update, context: CallbackContext) -> None:
    print(f"Received /start command from {update.effective_user.first_name}")
    update.message.reply_text(
        'Hello! Welcome to MiweLocker!\n\n'
        'Here are the available commands:\n'
        '/start - Start the bot and read this message.\n'
        '/commands - Get all bot commands.\n'
        '/guess <password> - Guess the password to get the flag.\n'
        '/pricing - Get current pricing.'
    )

def commands(update: Update, context: CallbackContext) -> None:
    print(f"Received /commands command from {update.effective_user.first_name}")
    message_template = (
        'Here are the available commands:\n'
        '/start - Start the bot and read this message.\n'
        '/flag - Get the flag.\n'
        '/commands - Get all bot commands.\n'
        '/guess <password> - Guess the password to get the flag.\n'
        '/pricing - Get current pricing.\n'
        'Remember: A command history is pasted into bin {PASTEBIN_ID} with password {PASTEBIN_PASSWORD}.'
    )
    message = message_template.format(PASTEBIN_ID=PASTEBIN_ID, PASTEBIN_PASSWORD=PASTEBIN_PASSWORD)
    update.message.reply_text(message)

def guess(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 1:
        guess = context.args[0]
        print(f"Received /guess command from {update.effective_user.first_name} with guess {guess}")
        if guess == PASSWORD:
            message_template = ('Correct! Here is your flag: {FLAG}')
            message = message_template.format(FLAG=FLAG)
            update.message.reply_text(message)
        else:
            update.message.reply_text('Wrong password.')
    else:
        print(f"Received invalid /guess command from {update.effective_user.first_name}")
        update.message.reply_text('Usage: /guess <password>')

def pricing(update: Update, context: CallbackContext) -> None:
    print(f"Received /pricing command from {update.effective_user.first_name}")
    update.message.reply_text('Current pricing: $500 per vic.')


def flag(update: Update, context: CallbackContext) -> None:
    print(f"Received /flag command from {update.effective_user.first_name}")
    update.message.reply_text('Haha, as if. Find the password.')

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("commands", commands))
    dispatcher.add_handler(CommandHandler("guess", guess))
    dispatcher.add_handler(CommandHandler("pricing", pricing))
    dispatcher.add_handler(CommandHandler("flag", flag))

    # Start the Bot
    print("Bot is now running...")
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()