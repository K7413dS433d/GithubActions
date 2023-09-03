import telebot
import sys
import os


# git the bot token from environment variables
Bot_Token = os.environ.get('TELEGRAM_BOT_TOKEN')

# git user id from environment variables
chat_id = os.environ.get('TELEGRAM_USER_ID')

bot = telebot.TeleBot(Bot_Token)  # create a bot instance


args = "".join(sys.argv[1:])  # take a commit info as an arguments from github


bot.send_message(chat_id, args)
