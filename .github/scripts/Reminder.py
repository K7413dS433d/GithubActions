import datetime
import requests
import os
import telebot


# git the bot token from environment variables
Reminder_Bot_Token = os.environ.get('K7413D_REMINDER_BOT_TOKEN')

# They said so api
# They_said_so_Token = os.environ.get('THEY_SAID_SO_TOKEN')

# Rabid api request 'Quotes'
Rapid_Api_Quotes_token = os.environ.get('RAPID_API_QUOTES_TOKEN')


# git user id from environment variables
chat_id = os.environ.get('TELEGRAM_USER_ID')


current_date = datetime.date.today()  # current date

current_day_name = current_date.strftime("%A")  # Full day name

requestRes = ""  # Request result
# They said so request ##########################################################################

# headers = {
#     'X-TheySaidSo-Api-Secret': f'{They_said_so_Token}'
# }

# response = requests.get("https://quotes.rest/qod", headers=headers)


# if response.status_code == 200:
#     data = response.json()
#     quote = data['contents']['quotes'][0]['quote']
#     author = data['contents']['quotes'][0]['author']
#     requestRes = f"{quote} \n Author: \n {author}"
# else:
#     requestRes = f"Api error with status code: {response.status_code} "

################################################################################################

# Rabid api request 'Quotes'####################################################################
url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": f'{Rapid_Api_Quotes_token}',
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    quote = data['content']
    author = data['originator']['name']
    requestRes = f"{quote} \n Author: \n {author}"
else:
    requestRes = f"Api error with status code: {response.status_code} "
################################################################################################


# handel the message
message1 = f'''{current_date}, {current_day_name} 🤷‍♂️
            Let’s go to gym :
                    Stay dedicated to see results 😊
'''
message2 = requestRes

# bot configuration

bot = telebot.TeleBot(Reminder_Bot_Token)  # create a bot instance

bot.send_message(chat_id, message1)  # send message to bot
bot.send_message(chat_id, message2)  # send message to bot
