#!/usr/bin/python

import telebot
import os
from dotenv import load_dotenv

load_dotenv()

HTTP_API = os.getenv('HTTP_API')

bot = telebot.TeleBot(HTTP_API)


# Handle '/start' and '/help'
#questa funzione viene eseguita quando si scrive /start
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.send_voice(message.chat.id, open('audio.mp3', 'rb'))


@bot.message_handler(commands=['qualecitta'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/qualecitta.mpeg', 'rb'))

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#questa funzione viene eseguita quando si scrive qualsiasi messaggio
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, 'Ciaoooooooo')


bot.polling()