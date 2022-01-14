import random
import time
from difflib import get_close_matches

import telebot

import alldata
import configure
import questiondata

bot = telebot.TeleBot('2071045701:AAFminFT9Q4ekEpTE2Aeo1-ZbU0nOFQ8ZAg')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет я хочу тебе помочь, напиши что хочешь знать о Польше и я тебе помогу!')
    time.sleep(2.75)
    bot.send_message(message.chat.id, 'Сейчас я помогу тебе разобраться с тем как я работаю')
    time.sleep(2.75)
    bot.send_message(message.chat.id,
                     'Ты можешь спросить меня о Польше просто написав в чате..\nПример: карта побыту, страховка, нужно ли сидеть карантин?, где я могу купить продукты в воскресенье?')


@bot.message_handler (content_types=['text'])
def get_messages(message):
    if message.text.lower() in alldata.alldataa:
        time.sleep(1.98)
        bot.send_message(message.chat.id, alldata.alldataa[message.text.lower()])
        i = 1
    elif len(get_close_matches(message.text.lower(), alldata.alldataa.keys())) > 0:
        time.sleep(1.98)
        bot.send_message(message.chat.id,
                         alldata.alldataa[get_close_matches(message.text.lower(), alldata.alldataa.keys())[0]])
        i = 1
    if message.text.lower() in questiondata.data and i !=1:
        time.sleep(1.98)
        bot.send_message(message.chat.id, questiondata.data[message.text.lower()])
        time.sleep(3)
        bot.send_message(message.chat.id, 'Что нибудь ещё?')
        time.sleep(1.5)
        bot.send_message(message.chat.id, f'Пример: {random.choice(list(tips.maybe.keys()))}')
    elif len(get_close_matches(message.text.lower(), questiondata.data.keys())) > 0:
        time.sleep(1.98)
        bot.send_message(message.chat.id,
                         questiondata.data[get_close_matches(message.text.lower(), questiondata.data.keys())[0]])
        time.sleep(3)
        bot.send_message(message.chat.id, 'Что нибудь ещё?')
        time.sleep(1.5)
        bot.send_message(message.chat.id, f'Пример: {random.choice(list(alldata.alldataa.keys()))}')
    elif len(get_close_matches(message.text.lower(), alldata.alldataa.keys())) <= 0:
        time.sleep(1.98)
        bot.send_message(message.chat.id, 'Я не могу понять о чём именно вы говорите')
        time.sleep(2.5)
        bot.send_message(message.chat.id,
                         'Если вас интересует конкретный вопрос вы можете его задать здесь\nhttps://docs.google.com/forms/d/e/1FAIpQLSeTsmDLgHzhmm7wTIr8SxDXzJFiZGpUROYLbBtQ0OG11MVLfw/viewform?usp=sf_link')
        time.sleep(2.75)
        bot.send_message(message.chat.id, 'Мы постараемся найти ответ на ваш вопрос, и добавить его в нашего бота\n:)')


bot.polling(none_stop=True, interval=0)
