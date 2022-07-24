import telebot
import os

from dotenv import load_dotenv
from telebot import types
load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет,<b> {message.from_user.first_name} <u>{message.from_user.last_name}</u> </b>'
    bot.send_message(message.chat.id, mess , parse_mode='html')


# @bot.message_handler(content_types='text')
# def get_user_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить', url='https://www.hirobots.spb.ru'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website_ = types.KeyboardButton('Вэб сайт')
    start_ = types.KeyboardButton('Start')

    markup.add(website_, start_)

    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

bot.polling(none_stop=True)





if __name__ == '__main__':
    pass



