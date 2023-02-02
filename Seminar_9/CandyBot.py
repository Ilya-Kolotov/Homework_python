import telebot
from telebot import types
import random
bot = telebot.TeleBot("6101089975:AAFjMl3OjWyxjWMqc9CVp0a6HbTvXlb7H2g")
user_turn = 0
bot_turn = 0
name1 = ''
name2 = 'bot'
flag = ''
sweets = 221
max_sweet = 28

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, "/help - Правила игры")
    bot.send_message(message.chat.id, "/go - Начало игры")
@bot.message_handler(commands = ["help"])
def help(message):
    bot.send_message(message.chat.id,"Привет! Это Игра с конфетами.\n\
Условия игры следующие:\n\
1) На столе лежит 221 конфета. Вы играете против Меня. Ходиv поочередно.\n\
2) Первый ход определяется жеребьёвкой.\n\
3) За один ход можно забрать не более чем 28 конфет, но не меньше 1.\n\
4) Все конфеты оппонента достаются сделавшему последний ход.\n\
Если условия понятны, то для начала игры, напишите команду:\n /go")


@bot.message_handler(commands=["go"])
def name_player(message):
    global name1
    bot.send_message(message.chat.id, "Начинаем игру")
    bot.send_message(message.chat.id, "Введите ваше имя")
    bot.register_next_step_handler(message, sentence)


@bot.message_handler(content_types="text")
def sentence(message):
    global name1
    text = message.text
    name1 = text
    choise_player(message)

@bot.message_handler(content_types="text")
def choise_player(message):
    global name1, flag, name2
    flag = random.choice([name1, name2])
    if flag == name1:
        bot.send_message(message.chat.id, f"Первым ходит - {flag}")
        bot.send_message(message.chat.id, f"На столе {sweets} конфет")
        controller(message)
    else:
        bot.send_message(message.chat.id, f"Первым ходит - {flag}")
        bot.send_message(message.chat.id, f"На столе {sweets} конфет")
        controller(message)

def controller(message):
    global flag, sweets
    if sweets > 0:
        if flag == name1:
            bot.send_message(message.chat.id, f"Ваш ход, {flag}, введите количество конфет от 1 до {max_sweet}")
            bot.register_next_step_handler(message, player_move)
        else:
            bot.send_message(message.chat.id, f"Сейчас ходит - {flag}")
            bot_move(message)
    else:
        flag = name1 if flag == name2 else name2
        bot.send_message(message.chat.id, f"Победил {flag}!")
        restart_game(message)

@bot.message_handler(content_types="text")
def player_move(message):
    global flag, sweets, user_turn
    user_turn = int(message.text)
    if not 0 < user_turn <= max_sweet:
        bot.send_message(message.chat.id, f'Введите конфеты в диапазоне от 1 до {max_sweet}')
        bot.register_next_step_handler(message, player_move)
    else:
        sweets -= user_turn
        bot.send_message(message.chat.id, f"Осталось {sweets} конфет")
        flag = name1 if flag == name2 else name2
        controller(message)

@bot.message_handler(content_types="text")
def bot_move(message):
    global sweets, flag, bot_turn
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"bot взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"Осталось {sweets} конфет")
    flag = name1 if flag == name2 else name2
    controller(message)

def restart_game(message):
    global  user_turn, bot_turn, name1, name2, flag, sweets, max_sweet
    user_turn = 0
    bot_turn = 0
    name1 = ''
    name2 = 'bot'
    flag = ''
    sweets = 221
    max_sweet = 28
    start(message)


bot.infinity_polling()
