import telebot
import configure
import os
import time
import telepot
from telepot.loop import MessageLoop
import random
import questiondata
import pprint
import cv2 as cv
import tempfile
import spwith
import tips
import urllib
import alldata
import csv
from textblob import TextBlob
from difflib import get_close_matches
from telebot import types

bot = telebot.TeleBot(configure.config['token'])
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет я хочу тебе помочь, напиши что хочешь знать о Польше и я тебе помогу!')
    time.sleep(2.75)
    bot.send_message(message.chat.id, 'Сейчас я помогу тебе разобраться с тем как я работаю')
    time.sleep(2.75)
    bot.send_message(message.chat.id, 'Ты можешь спросить меня о Польше просто написав в чате..\nПример: карта побыту, страховка, нужно ли сидеть карантин?, где я могу купить продукты в воскресенье?')

@bot.message_handler(content_types = ['text'])
def get_text(message):
    if message.text.lower() in spwith.speakdata:
        time.sleep(1.98)
        bot.send_message(message.chat.id, spwith.speakdata[message.text.lower()])
    elif len(get_close_matches(message.text.lower(), spwith.speakdata.keys())) > 0:
        time.sleep(1.98)
        bot.send_message(message.chat.id ,spwith.speakdata[get_close_matches(message.text.lower(), spwith.speakdata.keys())[0]])
    if message.text.lower() in questiondata.data:
        time.sleep(1.98)
        bot.send_message(message.chat.id, questiondata.data[message.text.lower()])
        time.sleep(3)
        bot.send_message(message.chat.id, 'Что нибудь ещё?')
        time.sleep(1.5)
        bot.send_message(message.chat.id, f'Пример: {random.choice(list(tips.maybe.keys()))}')
    elif len(get_close_matches(message.text.lower(), questiondata.data.keys())) > 0:
        time.sleep(1.98)
        bot.send_message(message.chat.id ,questiondata.data[get_close_matches(message.text.lower(), questiondata.data.keys())[0]])
        time.sleep(3)
        bot.send_message(message.chat.id, 'Что нибудь ещё?')
        time.sleep(1.5)
        bot.send_message(message.chat.id, f'Пример: {random.choice(list(tips.maybe.keys()))}')
    elif len(get_close_matches(message.text.lower(), alldata.alldataa.keys())) <= 0:
        time.sleep(1.98)
        bot.send_message(message.chat.id, 'Я не могу понять о чём именно вы говорите')
        time.sleep(2.5)
        bot.send_message(message.chat.id, 'Если вас интересует конкретный вопрос вы можете его задать здесь\nhttps://docs.google.com/forms/d/e/1FAIpQLSeTsmDLgHzhmm7wTIr8SxDXzJFiZGpUROYLbBtQ0OG11MVLfw/viewform?usp=sf_link')
        time.sleep(2.75)
        bot.send_message(message.chat.id, 'Мы постараемся найти ответ на ваш вопрос, и добавить его в нашего бота\n:)')

bot.polling(none_stop = True, interval = 0)
