from telebot import types
import telebot, time

token = '5150315371:AAFN9lYdkvvRm939u5Wgu0zh7qeRj9qCV8o'
q, a1, a2, a3, a4, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
nass = {}
bot = telebot.TeleBot(token)


# here are commands for hard mode in 'math quiz'
class QWSTMH:
    def qwstmh1(m):
        global a3
        a3 = 8
        if a3 == 8:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/-2")
            item2 = types.KeyboardButton("/2")
            item3 = types.KeyboardButton("/-1")
            item4 = types.KeyboardButton("/1")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'x/2+4x+5=0,5 | x=?', reply_markup=markup)
            a3 = 9

    def qwstmh2(m):
        global a3
        if a3 == 9:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/2,9")
            item2 = types.KeyboardButton("/1,7")
            item3 = types.KeyboardButton("/1,8")
            item4 = types.KeyboardButton("/0,8")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, '0,9/(1+1/8)=?', reply_markup=markup)
            a3 = 10

    def qwstmh3(m):
        global a3
        if a3 == 10:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/100000")
            item2 = types.KeyboardButton("/10000")
            item3 = types.KeyboardButton("/1000")
            item4 = types.KeyboardButton("/100")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, '27435/(1,55*1,77)=?', reply_markup=markup)
            a3 = 11

    def qwstmh4(m):
        global a3
        if a3 == 11:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/-550")
            item2 = types.KeyboardButton("/-650")
            item3 = types.KeyboardButton("/-600")
            item4 = types.KeyboardButton("/-500")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, '0,6*(-10)^3+50', reply_markup=markup)
            a3 = 12

    def qwstmh5(m):
        global a3
        if a3 == 12:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/-38")
            item2 = types.KeyboardButton("/16")
            item3 = types.KeyboardButton("/45")
            item4 = types.KeyboardButton("/11")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'x>=0', reply_markup=markup)
            bot.send_message(m.chat.id, '209(x+8)=209x+8(x^2+8x) | x=?', reply_markup=markup)
            a3 = 13

    def qwstmh6(m):
        global a3
        if a3 == 13:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/95")
            item2 = types.KeyboardButton("/85")
            item3 = types.KeyboardButton("/15")
            item4 = types.KeyboardButton("/40")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, '(3,4*3600)/144 = ?', reply_markup=markup)
            a3 = 14

    def qwstmh7(m):
        global a3
        if a3 == 14:
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/390")
            item2 = types.KeyboardButton("/600")
            item3 = types.KeyboardButton("/-780")
            item4 = types.KeyboardButton("/780")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            markup.add(item4)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, 'a=-39')
            bot.send_message(m.chat.id, '(a^3-25a)(1/(a+5)-1/(a-5))=?', reply_markup=markup)
            a3 = 15

    def wina3(m):
        global a3
        if a3 == 15:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/bravo")
            markup.add(item1)
            item2 = types.KeyboardButton("/menu")
            markup.add(item2)
            bot.send_message(m.chat.id, 'you win!!', reply_markup=markup)

    def losea3(m):
        global a3
        global a2
        if a3 > 0 or a2 > 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item2 = types.KeyboardButton("/menu")
            markup.add(item2)
            item1 = types.KeyboardButton("/let_me_cry")
            markup.add(item1)
            bot.send_message(m.chat.id, 'you lose!!', reply_markup=markup)
