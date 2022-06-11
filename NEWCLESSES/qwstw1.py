from telebot import types
import random, re, json, telebot, wikipedia, time, math

token = '5150315371:AAFN9lYdkvvRm939u5Wgu0zh7qeRj9qCV8o'
q, a1, a2, a3, a4, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
nass = {}
bot = telebot.TeleBot(token)


class QWSTW:
    def qwstw1(m):
        global a1
        a1 = 1
        if a1 == 1:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/Gorbachev")
            item2 = types.KeyboardButton("/Putin")
            item3 = types.KeyboardButton("/Lenin")
            item4 = types.KeyboardButton("/Stalin")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'Who wants to became millionaire!!!', reply_markup=markup)
            time.sleep(0.55)
            bot.send_message(m.chat.id, 'who was the first president of russia?', reply_markup=markup)
            a1 = 2

    def qwstw2(m):
        global a1
        if a1 == 2:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/seven")
            item2 = types.KeyboardButton("/six")
            item3 = types.KeyboardButton("/twelve")
            item4 = types.KeyboardButton("/eight")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'how many continents are there in the world?', reply_markup=markup)
            a1 = 3

    def qwstw3(m):
        global a1
        if a1 == 3:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/China-India")
            item2 = types.KeyboardButton("/France-Ukraine")
            item3 = types.KeyboardButton("/USA-Germany")
            item4 = types.KeyboardButton("/Russia-Vatican")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'the largest and smallest country?', reply_markup=markup)
            a1 = 4

    def qwstw4(m):
        global a1
        if a1 == 4:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/five")
            item2 = types.KeyboardButton("/four")
            item3 = types.KeyboardButton("/nine")
            item4 = types.KeyboardButton("/three")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'how many oceans are there in the world?', reply_markup=markup)
            a1 = 5

    def qwstw5(m):
        global a1
        if a1 == 5:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/kg_of_cotton")
            item2 = types.KeyboardButton("/the_same")
            item3 = types.KeyboardButton("/kg_of_metal")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'which is heavier, kg of metal or kg of cotton?', reply_markup=markup)
            a1 = 6

    def qwstw6(m):
        global a1
        if a1 == 6:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/tea")
            item2 = types.KeyboardButton("/coca-cola")
            item3 = types.KeyboardButton("/coffee")
            item4 = types.KeyboardButton("/water")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'the most popular drink in the world?', reply_markup=markup)
            a1 = 7

    def qwstw7(m):
        global a1
        if a1 == 7:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/rubiks_cube")
            item2 = types.KeyboardButton("/iPhone")
            item3 = types.KeyboardButton("/PlayStation")
            item4 = types.KeyboardButton("/Cars")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'the most popular product in the world?', reply_markup=markup)
            a1 = 8

    def wina1(m):
        global a1
        if a1 == 8:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/bravo")
            markup.add(item1)
            item2 = types.KeyboardButton("/menu")
            markup.add(item2)
            bot.send_message(m.chat.id, 'you win!!', reply_markup=markup)

    def losea1(m):
        global a1
        if a1 > 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item2 = types.KeyboardButton("/menu")
            markup.add(item2)
            item1 = types.KeyboardButton("/let_me_cry")
            markup.add(item1)
            bot.send_message(m.chat.id, 'you lose!!', reply_markup=markup)
