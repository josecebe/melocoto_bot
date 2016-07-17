#!/usr/bin/env python
# -*- coding: utf-8 -*-


import telebot 
from telebot import types 
import time
import sys, re, os, random
 
TOKEN = 'YOUR API KEY' 
 
bot = telebot.TeleBot(TOKEN)
 
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text': # Sólo saldrá en el log los mensajes tipo texto
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print mensaje
 
bot.set_update_listener(listener)

@bot.message_handler(commands=['x'])
def command_hola(m):
    cid = m.chat.id
    #bot.send_photo(cid, open("s.jpg", 'rb'))
    bot.send_message(cid, "hola")
 
bot.polling(none_stop=True)