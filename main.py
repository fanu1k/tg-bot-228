import telebot
from telebot import types
import sqlite3
from data import User

bot = telebot.TeleBot('1081604527:AAEg9RW1lGoNUjM9xojoa4mJuKPGclkB5yo')

currnum = None
dificult = None
name = None

variants = ['A', 'B', 'C']

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
'11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
'21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

answers = {
'1': 'A',
'2': 'C',
'3': 'C',
'4': 'C',
'5': 'C',
'6': 'C',
'7': 'C',
'8': 'A',
'9': 'A',
'10': 'C',
'11': 'C',
'12': 'B',
'13': 'B',
'14': 'C',
'15': 'A',
'16': 'A',
'17': 'B',
'18': 'B',
'19': 'B',
'20': 'C',
'21': 'B',
'22': 'B',
'23': 'C',
'24': 'C',
'25': 'B',
'26': 'C',
'27': 'C',
'28': 'C',
'29': 'A',
'30': 'C'
}

user = User(0, 0, 0, '0')


@bot.message_handler(commands=['start'])
def start_message(message):
    global complited
    global name
    name = user.get_login(message.chat.id, False)
    greeting = open('data/greeting.webp', 'rb')
    bot.send_sticker(message.chat.id, greeting)
    greeting.close()
    if name is None:
        bot.send_message(message.chat.id, 'Привет!')
        msg = bot.send_message(message.chat.id, 'Введите предпочитаемое имя пользователя')
        bot.register_next_step_handler(msg, register)
    else:
        bot.send_message(message.chat.id, 'Вы уже зарегестрированы')
        id = user.get_id(name[0], False)
        exp = user.get_exp(name[0], False)
        complited = user.get_complited(name[0], False)
        user.update_info(id, name[0], exp, complited)
        msg = bot.send_message(message.chat.id, 'Вперед!')
        main_menu(msg)

def register(message):
    chat_id = message.chat.id
    text = message.text
    if not (len(text) < 15):
        msg = bot.send_message(chat_id, 'incorrect login')
        bot.register_next_step_handler(msg, register)
        return
    user = User(chat_id, text, 0, 0)
    user.insert_user(chat_id, text)
    msg = bot.send_message(chat_id, 'Вперед!')
    main_menu(msg)

def main_menu(message):
    global user
    chat_id = message.chat.id
    text = message.text
    user = User(chat_id, text, 0, 0)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_play = types.KeyboardButton(text="Играть")
    button_file = types.KeyboardButton(text="Материалы")
    button_stat = types.KeyboardButton(text="Статистика")
    keyboard.add(button_play, button_file, button_stat)
    msg = bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=keyboard)

def lvl_choise(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_easy = types.KeyboardButton(text="Легкий")
    button_medium = types.KeyboardButton(text="Средний")
    button_hard = types.KeyboardButton(text="Сложный")
    keyboard.add(button_easy, button_medium, button_hard)
    txt = 'Выберите уровень сложности'
    msg = bot.send_message(message.chat.id, txt, reply_markup=keyboard)

def exer_choice(message, lvl=None):
    global dificult
    exers = None
    if lvl is not None:
        dificult = lvl
    if dificult == 'Легкий':
        exers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    elif dificult == 'Средний':
        exers = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    elif dificult == 'Сложный':
        exers = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_1 = types.KeyboardButton(text=exers[0])
    button_2 = types.KeyboardButton(text=exers[1])
    button_3 = types.KeyboardButton(text=exers[2])
    button_4 = types.KeyboardButton(text=exers[3])
    button_5 = types.KeyboardButton(text=exers[4])
    button_6 = types.KeyboardButton(text=exers[5])
    button_7 = types.KeyboardButton(text=exers[6])
    button_8 = types.KeyboardButton(text=exers[7])
    button_9 = types.KeyboardButton(text=exers[8])
    button_10 = types.KeyboardButton(text=exers[9])
    main_button = types.KeyboardButton(text='В главное меню')
    keyboard.add(
        button_1,
        button_2,
        button_3,
        button_4,
        button_5,
        button_6,
        button_7,
        button_8,
        button_9,
        button_10,
        main_button
        )
    msg = bot.send_message(message.chat.id, 'Выберите номер задания', reply_markup=keyboard)

def exercise(message, text):
    global currnum
    currnum = text
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_a = types.KeyboardButton(text="A")
    button_b = types.KeyboardButton(text="B")
    button_c = types.KeyboardButton(text="C")
    keyboard.add(button_a, button_b, button_c)
    number = open('exercises/{}.png'.format(text), 'rb')
    bot.send_photo(message.chat.id, number)
    number.close()
    msg = bot.send_message(message.chat.id, 'Выберите вариант ответа', reply_markup=keyboard)

def total(message, text):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    if answers[currnum] == text:
        stroka = "Правильный ответ!"
        user.change_complited(currnum)
    elif answers[currnum] != text:
        button_a = types.KeyboardButton(text="A")
        button_b = types.KeyboardButton(text="B")
        button_c = types.KeyboardButton(text="C")
        stroka = "Неправильный ответ"
        keyboard.add(button_a, button_b, button_c)
    exer_button = types.KeyboardButton(text='Выбрать другое задание')
    keyboard.add(exer_button)
    msg = bot.send_message(message.chat.id, stroka, reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def choise(message):
    global user
    global name
    if message.chat.type == 'private':
        if message.text == 'Играть':
            msg = bot.send_message(message.chat.id, 'Начнем!')
            lvl_choise(msg)
        elif message.text == 'Материалы':
            file = open('material/Классы.pdf', 'rb')
            file1 = open('material/Функции.pdf', 'rb')
            file2 = open('material/Основы.pdf', 'rb')
            msg = bot.send_document(message.chat.id, file)
            msg1 = bot.send_document(message.chat.id, file1)
            msg2 = bot.send_document(message.chat.id, file2)
            file.close()
            file1.close()
            file2.close()
        elif message.text == 'Статистика':
            info = user.get_complited(name[0], False)[0].replace('0', '')
            info = info.split('/')
            info = info[:-1]
            msg = bot.send_message(message.chat.id, 'Выполнено заданий: {}'.format(len(info)))
            msg = bot.send_message(message.chat.id, 'Выполненные задания: {}'.format(', '.join(info)))
        elif message.text == 'Легкий' and 'Средний' and 'Сложный':
            msg = bot.send_message(message.chat.id, 'Выбран {} уровень сложности'.format(message.text.lower()))
            exer_choice(msg, message.text)
        elif message.text == "В главное меню":
            msg = bot.send_message(message.chat.id, 'Возврат в главное меню')
            main_menu(msg)
        elif message.text in nums:
            msg = bot.send_message(message.chat.id, 'Вы выбрали задание {}'.format(message.text))
            exercise(msg, message.text)
        elif message.text in variants:
            msg = bot.send_message(message.chat.id, 'И это....')
            total(msg, message.text)
        elif message.text == 'Выбрать другое задание':
            msg = bot.send_message(message.chat.id, 'Переход к списку заданий')
            exer_choice(msg)



if __name__ == '__main__':
    bot.polling(none_stop=True)
