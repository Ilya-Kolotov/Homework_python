import telebot
from telebot import types
import datetime



bot = telebot.TeleBot("6198037503:AAH7kq-aDiaDl3RDAJlyJYAXE5zlRaHigLQ")

a = 0
b = 0
znak = ""
@bot.message_handler(commands=["start"])
def start(message):
    log(message)
    bot.send_message(message.chat.id, "Калькулятор включен!")
    button(message)


@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Целые числа")
    but2 = types.KeyboardButton("Комплексные числа")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выберите режим работы калькулятора", reply_markup=markup)


@bot.message_handler(content_types="text")
def controller(message):
    log(message)
    if message.text == "Целые числа":
        bot.send_message(message.chat.id, "Введите два числа через пробел(пример 10 8)")
        bot.register_next_step_handler(message, user_numbers_int)

    elif message.text == "Комплексные числа":
        bot.send_message(message.chat.id, "Введите два комплексных числа через пробел(пример, 2j 9 или 4j 8j)")
        bot.register_next_step_handler(message, user_numbers_complex)

def user_numbers_int(message):
    global a, b
    log(message)
    numbers = message.text
    if not numbers.split()[0].isdigit() or not numbers.split()[1].isdigit():
        bot.send_message(message.chat.id, "Ошибка! Введите два числа через пробел(пример 10 8)")
        bot.register_next_step_handler(message, user_numbers_int)
    else:
        a = int(numbers.split()[0])
        b = int(numbers.split()[1])
        button_znaki_int(message)
def user_numbers_complex(message):
    global a, b
    log(message)
    numbers = message.text
    a = complex(numbers.split()[0])
    b = complex(numbers.split()[1])
    button_znaki_complex(message)

def button_znaki_int(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    but5 = types.KeyboardButton("%")
    but6 = types.KeyboardButton("//")
    markup.row(but1, but2, but3)
    markup.row(but4, but5, but6)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
    bot.register_next_step_handler(message, operators_int)
def button_znaki_complex(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("+")
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("*")
    but4 = types.KeyboardButton("/")
    markup.row(but1, but2)
    markup.row(but3, but4)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
    bot.register_next_step_handler(message, operators_complex)


@bot.message_handler(content_types="text")
def operators_int(message):
    global a, b
    log(message)
    if message.text == "+":
        result = a + b
        bot.send_message(message.chat.id, f'{a} + {b} = {result}')
        restart_calc(message)
    if message.text == "-":
        result = a - b
        bot.send_message(message.chat.id, f'{a} - {b} = {result}')
        restart_calc(message)
    if message.text == "*":
        result = a * b
        bot.send_message(message.chat.id, f'{a} * {b} = {result}')
        restart_calc(message)
    if message.text == "/":
        result = a / b
        bot.send_message(message.chat.id, f'{a} / {b} = {result}')
        restart_calc(message)
    if message.text == "//":
        result = a // b
        bot.send_message(message.chat.id, f'{a} // {b} = {result}')
        restart_calc(message)
    if message.text == "%":
        result = a % b
        bot.send_message(message.chat.id, f'{a} % {b} = {result}')
        restart_calc(message)
@bot.message_handler(content_types="text")
def operators_complex(message):
    global a, b
    log(message)
    if message.text == "+":
        result = a + b
        bot.send_message(message.chat.id, f'{a} + {b} = {result}')
        restart_calc(message)
    if message.text == "-":
        result = a - b
        bot.send_message(message.chat.id, f'{a} - {b} = {result}')
        restart_calc(message)
    if message.text == "*":
        result = a * b
        bot.send_message(message.chat.id, f'{a} * {b} = {result}')
        restart_calc(message)
    if message.text == "/":
        result = a / b
        bot.send_message(message.chat.id, f'{a} / {b} = {result}')
        restart_calc(message)
def log(message):
    file = open('log.csv', 'a')
    file.write(f'{message.from_user.first_name};{message.text};{datetime.datetime.now().date()};{datetime.datetime.now().time().replace(microsecond = 0)}\n')
    file.close()
def restart_calc(message):
    global  a, b
    a = 0
    b = 0
    button(message)

bot.infinity_polling()