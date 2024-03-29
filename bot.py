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

@bot.message_handler(commands=['ueue'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/ueue.mp3', 'rb'))
    
@bot.message_handler(commands=['siaentrambe'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/sì_ad_entrambe_le_domande.mp3', 'rb'))
    
@bot.message_handler(commands=['perche'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/perche.mp3', 'rb'))
    
@bot.message_handler(commands=['scek'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/risata_scek.mp3', 'rb'))
    
@bot.message_handler(commands=['parenzoruttato'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/parenzo_rutto.mp3', 'rb'))
    
@bot.message_handler(commands=['parenzoruttato'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/mi_avete _rotto.mp3', 'rb'))
    
@bot.message_handler(commands=['cambiatoclima'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/ecambiatoilclimaschlein.mp3', 'rb'))
    
@bot.message_handler(commands=['bambalau'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/bambalau.mp3', 'rb'))
    
@bot.message_handler(commands=['parenzoghiaccio'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/parenzo_ghiaccio.mp3', 'rb'))
    
@bot.message_handler(commands=['meloni'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/meloni.mp3', 'rb'))
    
@bot.message_handler(commands=['chepalle'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/chepalle.mp3', 'rb'))

@bot.message_handler(commands=['chicacciaisoldi'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/chicacciaisoldi.mp3', 'rb'))
    
@bot.message_handler(commands=['chapureragionequesto'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/chapureragionequesto.mp3', 'rb'))
    
@bot.message_handler(commands=['pe'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/pe.mp3', 'rb'))
    
@bot.message_handler(commands=['staggente'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/staggente.mp3', 'rb'))
    
@bot.message_handler(commands=['cambiatoilclimaparenzo'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/cambiatoilclimaparenzo.mp3', 'rb'))
    
@bot.message_handler(commands=['chissene'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/chissene.mp3', 'rb'))
    
@bot.message_handler(commands=['vergogna'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/vergogna.mp3', 'rb'))
        
@bot.message_handler(commands=['basta'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/basta.mp3', 'rb'))
 
@bot.message_handler(commands=['finiamola'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/finiamola.mp3', 'rb'))
    
@bot.message_handler(commands=['gates'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/gates.mp3', 'rb'))
      
@bot.message_handler(commands=['unavergogna'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/una_vergogna.mp3', 'rb'))
    
@bot.message_handler(commands=['certo'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/certo.mp3', 'rb'))
    
@bot.message_handler(commands=['sniffata'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/sniffata.mp3', 'rb'))
    
    
@bot.message_handler(commands=['mascalzone'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/mascalzone.mp3', 'rb'))
    
    
@bot.message_handler(commands=['circonciso'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/circonciso.mp3', 'rb'))
    
    
@bot.message_handler(commands=['ottimo'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/ottimo.mp3', 'rb'))
    
    
@bot.message_handler(commands=['diciamolo'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/diciamolo.mp3', 'rb'))
    

@bot.message_handler(commands=['raccomandato'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/raccomandato.mp3', 'rb'))
    


@bot.message_handler(commands=['machecazzo'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/machecazzo.mp3', 'rb'))
    
@bot.message_handler(commands=['si'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/si.mp3', 'rb'))

@bot.message_handler(commands=['google'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/google.mp3', 'rb'))
    

@bot.message_handler(commands=['disgraziato'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/disgraziato.mp3', 'rb'))

@bot.message_handler(commands=['uou'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/uou.mp3', 'rb'))

@bot.message_handler(commands=['nitrito'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/nitrito.mp3', 'rb'))

@bot.message_handler(commands=['regolare'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/regolare.mp3', 'rb'))

@bot.message_handler(commands=['chiudi'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/chiudi_corto.mp3', 'rb'))

@bot.message_handler(commands=['fammelodire'])
def send_welcome(message):
    bot.send_voice(message.chat.id, open('audio/fammelo_dire.mp3', 'rb'))

bot.polling()
