import telebot
from telebot import types
import sqlite3
from data import User

bot = telebot.TeleBot('1265769270:AAEW4OJS-8ZvCB272gtHCSx_RLwids1llcc')

user = User(0, 0, 0, '0')


@bot.message_handler(commands=['start'])
def start_message(message):
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        "SELECT Login FROM database WHERE ID = '%s'" % message.chat.id).fetchone()
    con.close()
    greeting = open('data/greeting.webp', 'rb')
    bot.send_sticker(message.chat.id, greeting)
    if result is None:
        bot.send_message(message.chat.id, 'Приветствие')
        msg = bot.send_message(message.chat.id, 'Введите предпочитаемое имя пользователя')
        bot.register_next_step_handler(msg, register)
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегестрированны')
        id = user.get_id(result[0], False)
        exp = user.get_exp(result[0], False)
        complited = user.get_complited(result[0], False)
        user.update_info(id, result[0], exp, complited)


def register(message):
    global user
    chat_id = message.chat.id
    text = message.text
    if not (5 < len(text) < 15):
        msg = bot.send_message(chat_id, 'incorrect login')
        bot.register_next_step_handler(msg, register)
        return
    con = sqlite3.connect('user_database.db')
    cur = con.cursor()
    result = cur.execute(
        "INSERT INTO database (ID, Login, Exp, Completed) VALUES ('%s', '%s', '%s', '%s')" % (chat_id, text, 0, 0))
    con.commit()
    con.close()
    user = User(chat_id, text, 0, 0)
    msg = bot.send_message(chat_id, 'Добро пожаловть ' + text)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_pay = types.KeyboardButton(text="Пройти тест")
    button_file = types.KeyboardButton(text="Начать с нуля")
    keyboard.add(button_pay, button_file)
    txt = "Вы можете пройти тест на знание python, либо начать с начала"
    msg = bot.send_message(message.chat.id, txt, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def choise(message):
    global user
    if message.chat.type == 'private':
        if message.text == 'Пройти тест':
            pass
        elif message.text == 'Начать с нуля':
            user.set_info()
            print('Привет')


def test(message):
    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
