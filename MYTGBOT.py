from telebot import types
import random, re, json, telebot, wikipedia, time, math
from NEWCLESSES.qwstw1 import QWSTW
from NEWCLESSES.qwstme import QWSTME
from NEWCLESSES.qwstmh import QWSTMH
from NEWCLESSES.cartriges import CARTRIGES
from NEWCLESSES.othercommands import commands

# all needed imports
token = '5150315371:AAFN9lYdkvvRm939u5Wgu0zh7qeRj9qCV8o'
wikipedia.set_lang('ru')
q, a1, a2, a3, a4, a5, a, b, c = 0, 0, 0, 0, 0, 0, 0, 0, 0
nass = {}
bot = telebot.TeleBot(token)


# for telegramm


# only for better experience of using bot
@bot.message_handler(commands=["start"])
def start(m):
    commands.start(m)


@bot.message_handler(commands=["menu"])
def menu(m):
    commands.menu(m)


# only for better experience of using bot
@bot.message_handler(commands=["who_wants_to_become_a_millionaire"])
def start_who_wants_to_become_a_millionaire(m):
    commands.start_new(m)


@bot.message_handler(commands=["math_quiz"])
def start_math_quiz(m):
    commands.start_new2(m)


@bot.message_handler(commands=["russian_roulette"])
def start_russian_roulette(m):
    commands.start_new3(m)


# 3 main games
# HERE ALL COMMANDS FOR 'who_wants_to_become_a_millionaire'
# but 'not_now' for all of games
@bot.message_handler(commands=["not_now"])
def no(m):
    commands.no(m)


@bot.message_handler(commands=["yes"])
def ssqwstw1(m):
    QWSTW.qwstw1(m)


@bot.message_handler(commands=["Putin"])
def ssqwstw2(m):
    QWSTW.qwstw2(m)


@bot.message_handler(commands=["seven"])
def ssqwstw3(m):
    QWSTW.qwstw3(m)


@bot.message_handler(commands=["Russia-Vatican"])
def ssqwstw4(m):
    QWSTW.qwstw4(m)


@bot.message_handler(commands=["five"])
def ssqwstw5(m):
    QWSTW.qwstw5(m)


@bot.message_handler(commands=["the_same"])
def ssqwstw6(m):
    QWSTW.qwstw6(m)


@bot.message_handler(commands=["tea"])
def ssqwstw7(m):
    QWSTW.qwstw7(m)


# i use 'strange' command like '/tea' because i cant imagine other ways how to do it ^-^
@bot.message_handler(commands=["iPhone"])
def sswina1(m):
    QWSTW.wina1(m)


# also, there are many commands to lose game, only if your answer were wrong
@bot.message_handler(
    commands=["lose", 'Gorbachev', 'Lenin', 'Stalin', 'eight', 'twelve', 'six', 'China-India', 'France-Ukraine ',
              'USA-Germany', 'nine', 'four', 'three', 'kg_of_cotton', 'kg_of_metal', 'water', 'coffee', 'coca-cola',
              'Cars', 'PlayStation', 'rubiks_cube'])
def sslosea1(m):
    QWSTW.losea1(m)


# HERE ALL COMMANDS FOR 'math quiz'
@bot.message_handler(commands=["lets_go"])
def qwstm(m):
    commands.qwstm(m)


# You can change complexity ^-^
@bot.message_handler(commands=["easy"])
def ssqwstme1(m):
    QWSTME.qwstme1(m)


@bot.message_handler(commands=["a*a+b*b=c*c"])
def ssqwstme2(m):
    QWSTME.qwstme2(m)


@bot.message_handler(commands=["13"])
def ssqwstme3(m):
    QWSTME.qwstme3(m)


@bot.message_handler(commands=["625"])
def ssqwstme4(m):
    QWSTME.qwstme4(m)


@bot.message_handler(commands=["1000kg"])
def ssqwstme5(m):
    QWSTME.qwstme5(m)


@bot.message_handler(commands=["-0,9905"])
def sswin_a2(m):
    QWSTME.win_a2(m)


@bot.message_handler(commands=["hard"])
def ssqwstmh1(m):
    QWSTMH.qwstmh1(m)


@bot.message_handler(commands=["-1"])
def ssqwstmh2(m):
    QWSTMH.qwstmh2(m)


@bot.message_handler(commands=["0,8"])
def ssqwstmh3(m):
    QWSTMH.qwstmh3(m)


@bot.message_handler(commands=["10000"])
def ssqwstmh4(m):
    QWSTMH.qwstmh4(m)


@bot.message_handler(commands=["-550"])
def ssqwstmh5(m):
    QWSTMH.qwstmh5(m)


@bot.message_handler(commands=["11"])
def ssqwstmh6(m):
    QWSTMH.qwstmh6(m)


@bot.message_handler(commands=["85"])
def ssqwstmh7(m):
    QWSTMH.qwstmh7(m)


@bot.message_handler(commands=["390"])
def sswina3(m):
    QWSTMH.wina3(m)


@bot.message_handler(
    commands=["lose", '600', '-780', '780', '40', '15', '95', '45', '16', '-38', '-500', '-600', '-650', '100', '1000',
              '100000', '1,8', '1,7', '2,9', '1', '2',
              '-2', '-0,9805', '-0,9806', '-0,9804', '100kg', '1000g', '100000g', '3025', '525', '50', '16', '17', '19',
              'a*c+b*c=a*b*c', 'a*b+a*b=c*c', 'a*a-b*b=c*c'])
def sslosea3(m):
    QWSTMH.losea3(m)


# Also there are 'extra mode', where you can solve equations, but they often are unsolvable(

@bot.message_handler(commands=["extra_mode"])
def extra_mode(m):
    commands.extra_mode(m)


@bot.message_handler(commands=["lets_start"])
def extra_mode(m):
    commands.extra_mode1(m)


@bot.message_handler(commands=["new_try"])
def extra_mode(m):
    commands.extra_mode1(m)


@bot.message_handler(commands=["view_the_answer"])
def extra_mode_answer(m):
    commands.extra_mode_answer(m)


# HERE ALL COMMANDS FOR 'russian roulette'
@bot.message_handler(commands=["ok"])
def rr(m):
    commands.rr(m)


@bot.message_handler(commands=["1_cartridge"])
def ssrr1c(m):
    CARTRIGES.rr1c(m)


@bot.message_handler(commands=["2_cartridges"])
def ssrr2c(m):
    CARTRIGES.rr2c(m)


@bot.message_handler(commands=["3_cartridges"])
def ssrr3c(m):
    CARTRIGES.rr3c(m)


@bot.message_handler(commands=["4_cartridges"])
def ssrr4c(m):
    CARTRIGES.rr4c(m)


@bot.message_handler(commands=["5_cartridges"])
def ssrr5c(m):
    CARTRIGES.rr5c(m)


# several commands just for fun

@bot.message_handler(commands=["let_me_cry"])
def let_me_cry(m):
    commands.let_me_cry(m)


@bot.message_handler(commands=["bravo"])
def bravo(m):
    commands.bravo(m)


# so that it does not interfere, you can search for words only when you have entered the word search mode
@bot.message_handler(commands=["word_search"])
def search(m):
    commands.search(m)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    commands.handle_text(message)


bot.polling(none_stop=True, interval=0)
