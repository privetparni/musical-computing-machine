from telebot import types
import telebot, time

token = '5150315371:AAFN9lYdkvvRm939u5Wgu0zh7qeRj9qCV8o'
q, a1, a2, a3, a4, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
nass = {}
bot = telebot.TeleBot(token)


# here are commands for easy mode in 'math quiz'
class QWSTME:
    def qwstme1(m):
        global a2
        if a2 == 2:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            time.sleep(1)
            item1 = types.KeyboardButton("/a*a+b*b=c*c")
            item2 = types.KeyboardButton("/a*a-b*b=c*c")
            item3 = types.KeyboardButton("/a*b+a*b=c*c")
            item4 = types.KeyboardButton("/a*c+b*c=a*b*c")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item10 = types.KeyboardButton("/menu")
            markup.add(item10)
            bot.send_message(m.chat.id, 'the correct pythagorean theorem?', reply_markup=markup)
            a2 = 3

    def qwstme2(m):
        global a2
        if a2 == 3:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/17")
            item2 = types.KeyboardButton("/13")
            item3 = types.KeyboardButton("/16")
            item4 = types.KeyboardButton("/19")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'the root of the number 169?', reply_markup=markup)
            a2 = 4

    def qwstme3(m):
        global a2
        if a2 == 4:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/3025")
            item2 = types.KeyboardButton("/50")
            item3 = types.KeyboardButton("/525")
            item4 = types.KeyboardButton("/625")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, '25^2?', reply_markup=markup)
            a2 = 5

    def qwstme4(m):
        global a2
        if a2 == 5:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/100000g")
            item2 = types.KeyboardButton("/1000g")
            item3 = types.KeyboardButton("/1000kg")
            item4 = types.KeyboardButton("/100kg")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'in one ton?', reply_markup=markup)
            a2 = 6

    def qwstme5(m):
        global a2
        if a2 == 6:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/-0,9804")
            item2 = types.KeyboardButton("/-0,9806")
            item3 = types.KeyboardButton("/-0,9805")
            item4 = types.KeyboardButton("/-0,9905")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, '0,3+0,01+0,0005-1,301', reply_markup=markup)
            a2 = 7

    def win_a2(m):
        global a2
        if a2 == 7:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/bravo")
            markup.add(item1)
            item2 = types.KeyboardButton("/menu")
            markup.add(item2)
            bot.send_message(m.chat.id, 'you win!!', reply_markup=markup)
