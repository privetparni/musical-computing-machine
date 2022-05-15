import re
import telebot
import wikipedia

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
    wikikey1 = message.text
    wikikey = f'https://ru.wikipedia.org/wiki/{wikikey1}'
    # не работает
    #key = message.text
    #img = f'http://kraski-zhizni.com/wp-content/uploads/2020/06/IMG_4418.jpeg'
    # НЕ РАБОТАЕТ
    bot.send_photo(message.chat.id, wikikey)


bot.polling(none_stop=True, interval=0)
