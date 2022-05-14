import re
import telebot
import wikipedia
from base64 import b64decode

from selenium import webdriver
token = '5150315371:AAFN9lYdkvvRm939u5Wgu0zh7qeRj9qCV8o'

bot = telebot.TeleBot(token)
wikipedia.set_lang("ru")


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


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, fwiki(message.text))

    key = message.text
    img = f'https://www.google.ru/search?q={key}&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X'

    bot.send_photo(message.chat.id, img)


bot.polling(none_stop=True, interval=0)
