import telebot
import sys
import os
import datetime
import pytz


# git the bot token from environment variables
Bot_Token = os.environ.get('TELEGRAM_BOT_TOKEN')

# git user id from environment variables
chat_id = os.environ.get('TELEGRAM_USER_ID')

bot = telebot.TeleBot(Bot_Token)  # create a bot instance


args = "".join(sys.argv[1:])  # take a commit info as an arguments from github

egypt_timezone = pytz.timezone('Africa/Cairo') # Egyptian time zone

current_datetime = datetime.datetime.now(egypt_timezone)  # current date and time

current_day_name = current_datetime.strftime("%A")  # Full day name

formatted_time = current_datetime.strftime(
    '%I:%M %p')  # 12-hour time format with AM/PM

message = f"{current_day_name} on {current_datetime.strftime('%Y-%m-%d')} at {formatted_time}\n\n {args}"


bot.send_message(chat_id, message)
