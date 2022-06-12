from telebot import types
import random, telebot, time

token = '5150315371:AAFN9lYdkvvRm939u5Wgu0zh7qeRj9qCV8o'
q, a1, a2, a3, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0
nass = {}
bot = telebot.TeleBot(token)


# Here are commands only for 'russian roulette'
class CARTRIGES:
    def rr1c(m):
        global a4
        if a4 == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/menu")
            markup.add(item1)
            item2 = types.KeyboardButton("/1_cartridge")
            markup.add(item2)
            revolver_drum = [0, 0, 0, 0, 0, 1]
            k = random.choice(revolver_drum)
            if k == 1:
                bot.send_message(m.chat.id, 'You DIE!!!')
            else:
                bot.send_message(m.chat.id, 'You ALIVE!!!')
            time.sleep(1)
            bot.send_message(m.chat.id, 'to try again, click "/1_cartridge"', reply_markup=markup)

    def rr2c(m):
        global a4
        if a4 == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/menu")
            markup.add(item1)
            item2 = types.KeyboardButton("/2_cartridges")
            markup.add(item2)
            revolver_drum = [0, 0, 0, 0, 1, 1]
            k = random.choice(revolver_drum)
            if k == 1:
                bot.send_message(m.chat.id, 'You DIE!!!')
            else:
                bot.send_message(m.chat.id, 'You ALIVE!!!')
            time.sleep(1)
            bot.send_message(m.chat.id, 'to try again, click "/2_cartridges"', reply_markup=markup)

    def rr3c(m):
        global a4
        if a4 == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/menu")
            markup.add(item1)
            item2 = types.KeyboardButton("/3_cartridges")
            markup.add(item2)
            revolver_drum = [0, 0, 0, 1, 1, 1]
            k = random.choice(revolver_drum)
            if k == 1:
                bot.send_message(m.chat.id, 'You DIE!!!')
            else:
                bot.send_message(m.chat.id, 'You ALIVE!!!')
            time.sleep(1)
            bot.send_message(m.chat.id, 'to try again, click "/3_cartridges"', reply_markup=markup)

    def rr4c(m):
        global a4
        if a4 == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/menu")
            markup.add(item1)
            item2 = types.KeyboardButton("/4_cartridges")
            markup.add(item2)
            revolver_drum = [0, 0, 1, 1, 1, 1]
            k = random.choice(revolver_drum)
            if k == 1:
                bot.send_message(m.chat.id, 'You DIE!!!')
            else:
                bot.send_message(m.chat.id, 'You ALIVE!!!')
            time.sleep(1)
            bot.send_message(m.chat.id, 'to try again, click "/4_cartridges"', reply_markup=markup)

    def rr5c(m):
        global a4
        if a4 == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/menu")
            markup.add(item1)
            item2 = types.KeyboardButton("/5_cartridges")
            markup.add(item2)
            revolver_drum = [0, 1, 1, 1, 1, 1]
            k = random.choice(revolver_drum)
            if k == 1:
                bot.send_message(m.chat.id, 'You DIE!!!')
            else:
                bot.send_message(m.chat.id, 'You ALIVE!!!')
            time.sleep(1)
            bot.send_message(m.chat.id, 'to try again, click "/5_cartridges"', reply_markup=markup)

    def rr(m):
        global a4
        a4 = 1
        if a4 == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/menu")
            markup.add(item1)
            item2 = types.KeyboardButton("/1_cartridge")
            markup.add(item2)
            item3 = types.KeyboardButton("/2_cartridges")
            markup.add(item3)
            item4 = types.KeyboardButton("/3_cartridges")
            markup.add(item4)
            item5 = types.KeyboardButton("/4_cartridges")
            markup.add(item5)
            item6 = types.KeyboardButton("/5_cartridges")
            markup.add(item6)
            bot.send_message(m.chat.id, 'select the number of rounds', reply_markup=markup)