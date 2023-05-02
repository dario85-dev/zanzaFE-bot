#!/usr/bin/python

import telebot
from telebot import custom_filters
import os
from dotenv import load_dotenv

load_dotenv()

HTTP_API = os.getenv('HTTP_API')

bot = telebot.TeleBot(HTTP_API)


@bot.message_handler(commands=['qualecitta'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/qualecitta.mpeg', 'rb'))
    
    

@bot.message_handler(commands=['ali'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/ali.mpeg', 'rb'))

@bot.message_handler(commands=['beh'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/beh.mpeg', 'rb'))

@bot.message_handler(commands=['chicazzosei'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/chicazzosei.mpeg', 'rb'))

@bot.message_handler(commands=['finiamola'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/finiamola.mpeg', 'rb'))

@bot.message_handler(commands=['friccica'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/friccica.mpeg', 'rb'))

@bot.message_handler(commands=['frocioni'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/frocioni.mpeg', 'rb'))

@bot.message_handler(commands=['haragione'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/haragione.mpeg', 'rb'))

@bot.message_handler(commands=['intervento'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/intervento.mpeg', 'rb'))

@bot.message_handler(commands=['parenzocombatti'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/parenzocombatti.mpeg', 'rb'))

@bot.message_handler(commands=['possibilissimo'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/possibilissimo.mpeg', 'rb'))

@bot.message_handler(commands=['ali'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/ali.mpeg', 'rb'))

@bot.message_handler(commands=['seicambiata'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/seicambiata.mpeg', 'rb'))

@bot.message_handler(commands=['sisisi'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/sisisi.mpeg', 'rb'))

@bot.message_handler(commands=['tonycasabianca'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/tonycasabianca.mpeg', 'rb'))

@bot.message_handler(commands=['vaiacagare'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/vaiacagare.mpeg', 'rb'))

@bot.message_handler(commands=['zittopino'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/zittopino.mpeg', 'rb'))

@bot.message_handler(commands=['valutazionepeni'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/valutazionepeni.mpeg', 'rb'))






bot.polling()
