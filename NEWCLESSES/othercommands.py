from telebot import types
import random, re, json, telebot, wikipedia, time, math

token = '5150315371:AAFN9lYdkvvRm939u5Wgu0zh7qeRj9qCV8o'
q, a1, a2, a3, a4, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
nass = {}
bot = telebot.TeleBot(token)


# Here are main command for bot
# some of them are just for fun

def fwiki(s):
    try:
        qwe = wikipedia.page(s)
        wikitext = qwe.content[:600]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if len((x.strip())) > 3:
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2

    except Exception as e:
        return 'В энциклопедии нет информации об этом'


class commands:
    def start(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        global q, a1, a2, a3, a4, a5, a, b, c
        q, a1, a2, a3, a4, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
        item1 = types.KeyboardButton("/word_search")
        markup.add(item1)
        item2 = types.KeyboardButton("/who_wants_to_become_a_millionaire")
        markup.add(item2)
        item2 = types.KeyboardButton("/math_quiz")
        markup.add(item2)
        item3 = types.KeyboardButton("/russian_roulette")
        markup.add(item3)
        item4 = types.KeyboardButton("/menu")
        markup.add(item4)
        bot.send_message(m.chat.id, 'Hello!', reply_markup=markup)
        print(nass)
        time.sleep(1)
        bot.send_message(m.chat.id, 'Look what I can do:', reply_markup=markup)
        with open("temp.json", "w", encoding="utf-8") as file:
            json.dump(nass, file)

    def menu(m):
        global q, a1, a2, a3, a4, a5, a, b, c
        q, a1, a2, a3, a4, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/word_search")
        markup.add(item1)
        item2 = types.KeyboardButton("/who_wants_to_become_a_millionaire")
        markup.add(item2)
        item2 = types.KeyboardButton("/math_quiz")
        markup.add(item2)
        item3 = types.KeyboardButton("/russian_roulette")
        markup.add(item3)
        item4 = types.KeyboardButton("/menu")
        markup.add(item4)
        bot.send_message(m.chat.id, 'look:', reply_markup=markup)
        print(nass)
        with open("temp.json", "w", encoding="utf-8") as file:
            json.dump(nass, file)

    def start_new(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/yes")
        item2 = types.KeyboardButton("/not_now")
        markup.add(item1)
        markup.add(item2)
        item3 = types.KeyboardButton("/menu")
        markup.add(item3)
        bot.send_message(m.chat.id, 'Lets play "Who wants to became millionaire"?', reply_markup=markup)

    def start_new2(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/lets_go")
        item2 = types.KeyboardButton("/not_now")
        markup.add(item1)
        markup.add(item2)
        item3 = types.KeyboardButton("/menu")
        markup.add(item3)
        bot.send_message(m.chat.id, 'Lets play "math quiz"?', reply_markup=markup)

    def start_new3(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/ok")
        item2 = types.KeyboardButton("/not_now")
        markup.add(item1)
        markup.add(item2)
        item3 = types.KeyboardButton("/menu")
        markup.add(item3)
        bot.send_message(m.chat.id, 'Lets play "russian roulette"?', reply_markup=markup)

    def no(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/menu")
        markup.add(item1)
        bot.send_message(m.chat.id, 'maybe next time(', reply_markup=markup)

    def qwstm(m):
        global a2
        a2 = 1
        if a2 == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item10 = types.KeyboardButton("/menu")
            markup.add(item10)
            bot.send_message(m.chat.id, 'math quiz!!!')
            item1 = types.KeyboardButton("/easy")
            item2 = types.KeyboardButton("/hard")
            item3 = types.KeyboardButton("/extra_mode")
            markup.add(item1)
            markup.add(item2)
            markup.add(item3)
            bot.send_message(m.chat.id, 'choose mode:', reply_markup=markup)
            a2 = 2

    def extra_mode(m):
        global a5
        a5 = 1
        time.sleep(0.25)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/lets_start")
        markup.add(item1)
        item5 = types.KeyboardButton("/menu")
        markup.add(item5)
        bot.send_message(m.chat.id,
                         'now the bot will send random quadratic equations, and you will solve them, after which you will '
                         'be able to check your answer',
                         reply_markup=markup)

    def extra_mode1(m):
        if a5 > 0:
            global a, b, c
            aa1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            bb1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            cc1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            a = random.choice(aa1)
            b = random.choice(bb1)
            c = random.choice(cc1)
            time.sleep(0.25)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("/view_the_answer")
            markup.add(item1)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)
            bot.send_message(m.chat.id, f'{a}x^2+{b}x+{c}=0', reply_markup=markup)

    def extra_mode_answer(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if a5 > 0:
            global a, b, c
            time.sleep(0.25)
            discr = b ** 2 - 4 * a * c
            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                bot.send_message(m.chat.id, "x1 = %.2f  x2 = %.2f" % (x1, x2))
            elif discr == 0:
                x = -b / (2 * a)
                bot.send_message(m.chat.id, "x = %.2f" % x)
            else:
                bot.send_message(m.chat.id, "there are no roots")
            item3 = types.KeyboardButton("/new_try")
            markup.add(item3)
            item5 = types.KeyboardButton("/menu")
            markup.add(item5)

        bot.send_message(m.chat.id, 'if you want to solve another equation, click on "/new_try"', reply_markup=markup)

    def let_me_cry(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("/menu")
        markup.add(item2)
        item1 = types.KeyboardButton("/let_me_cry")
        markup.add(item1)
        bot.send_message(m.chat.id, '😭😭😭', reply_markup=markup)

    def bravo(m):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/bravo")
        markup.add(item1)
        item2 = types.KeyboardButton("/menu")
        markup.add(item2)
        bot.send_message(m.chat.id, '🎆🎇🎆', reply_markup=markup)

    def search(m):
        global q
        q = 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("/menu")
        markup.add(item2)
        bot.send_message(m.chat.id, 'Just send me message (preferably in Russian)', reply_markup=markup)

    def handle_text(message):
        global q
        user_id = message.from_user.id
        nass[user_id] = message.text
        if q == 1:
            bot.send_message(message.chat.id, "here's what I managed to find:")
            bot.send_message(message.chat.id, fwiki(message.text))
            wikikey = message.text
            bot.send_message(message.chat.id, f'https://ru.wikipedia.org/wiki/{wikikey}')
        with open("temp.json", "w", encoding="utf-8") as file:
            json.dump(nass, file)
        print(nass)
