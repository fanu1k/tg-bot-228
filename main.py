import telebot
from telebot import types

bot = telebot.TeleBot('1265769270:AAEW4OJS-8ZvCB272gtHCSx_RLwids1llcc')


@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.id not in "base":
        bot.send_message(message.chat.id, 'Приветствие')
        msg = bot.send_message(message.chat.id, 'Введите предпочитаемое имя пользователя')
        bot.register_next_step_handler(msg, register)
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегестрированны')


def register(message):
    chat_id = message.chat.id
    text = message.text
    if not '''проверки логина''':
        msg = bot.send_message(chat_id, 'incorrect login')
        bot.register_next_step_handler(msg, register)
        return
    # Логин в базу
    msg = bot.send_message(chat_id, 'Добро пожаловть ' + text)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_pay = types.KeyboardButton(text="Пройти тест")
    button_file = types.KeyboardButton(text="Начать с нуля")
    keyboard.add(button_pay, button_file)
    msg = bot.send_message(message.chat.id, "Вы можете пройти тест на знание python, либо начать с начала", reply_markup=keyboard)
    bot.register_next_step_handler(msg, choise)


def choise(message):
    if message.text == 'Пройти тест':
        # Тест
    if message.text == 'Начать с нуля':
        # Игра


if __name__ == '__main__':
    bot.polling(none_stop=True)
