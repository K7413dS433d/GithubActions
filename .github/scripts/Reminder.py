import datetime
import requests
import os
import telebot


# git the bot token from environment variables
Bot_Token = os.environ.get('K7413D_REMINDER_BOT_TOKEN')

# They said so api
Tey_said_so_Token = os.environ.get('THEY_SAID_SO_TOKEN')


# git user id from environment variables
chat_id = os.environ.get('TELEGRAM_USER_ID')


current_date = datetime.date.today()  # current date

current_day_name = current_date.strftime("%A")  # Full day name


# They said so request
requestRes = ""  # Request result


headers = {
    'X-TheySaidSo-Api-Secret': f'{Tey_said_so_Token}'
}

response = requests.get("https://quotes.rest/qod", headers=headers)


if response.status_code == 200:
    data = response.json()
    quote = data['contents']['quotes'][0]['quote']
    author = data['contents']['quotes'][0]['author']
    requestRes = f"{quote} \n Author: \n {author}"
else:
    requestRes = f"Error with api with status code {response.status_code} "



# handel the message
message1 = f'''{current_date}, {current_day_name} 🤷‍♂️
            Let’s go to gym :
                    Stay dedicated to see results 😊
'''
message2 = requestRes

# bot configuration

bot = telebot.TeleBot(Bot_Token)  # create a bot instance

bot.send_message(chat_id, message1)  # send message to bot
bot.send_message(chat_id, message2)  # send message to b