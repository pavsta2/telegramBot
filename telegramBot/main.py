import os
import re
import requests
import logging

import telebot
from yaweather import YaWeather, Russia
from translate import Translator
from dotenv import load_dotenv
from telebot import types

load_dotenv()

token = os.getenv('TOKEN')  # получаем токен из переменных окружения
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')  # получаем токен api yandex погоды из переменных окружения
bot = telebot.TeleBot(token)  # создаем экземпляр бота
logging.basicConfig(level=logging.WARNING,
                    filename='botlogs.log',
                    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: "
                           "%(lineno)d - %(message)s", datefmt='%H:%M:%S', )


# создаем декорированную функцию для обработки сообщений от пользователя
@bot.message_handler(commands=['start', 'MENU'])
def start(message):
    hello_mess = f'Здравствуйте, {message.from_user.first_name}!\n Я бот-помощник сети детских клубов HiROBOTS. ' \
                 f'Задайте Ваш вопрос или напишите мне цифру, соответствующую интересующему Вас вопросу: \n'
    with open("menu_mess.txt", encoding="utf-8") as f:
        menu_mess = f.read()
    mess = hello_mess + menu_mess

    # bot.send_message(message.chat.id, message)

    markup_rkm = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_main_menu = types.KeyboardButton('/MENU')
    markup_rkm.add(btn_main_menu)

    bot.send_message(message.chat.id, mess, reply_markup=markup_rkm)


@bot.message_handler(content_types='text')
def got_text(message):
    text = message.text.lower()  # получаем текст строчными буквами

    # вопросы про расписание занятий
    if re.search(r'расписани', text) is not None or text == '2':
        # markup_shed = types.InlineKeyboardMarkup(row_width=1)
        # btn_avia = types.InlineKeyboardButton('пр.Авиаконструкторов д.2',
        #                                       url='https://www.hirobots.spb.ru/raspisanie-kulba-aviakonstruktorov')
        # btn_gash = types.InlineKeyboardButton('ул.Ярослава Гашека д.17',
        #                                       url='https://www.hirobots.spb.ru/raspisanie-kluba-gasheka')
        # btn_vo = types.InlineKeyboardButton('Малый пр.В.О. д.88',
        #                                     url='https://www.hirobots.spb.ru/расписание-клуба-василеостровский')
        #
        # markup_shed.add(btn_avia, btn_gash, btn_vo)
        # bot.send_message(message.chat.id, 'Выберите адрес клуба:', reply_markup=markup_shed)
        photo1 = open('photo/kupchino 22-23 - 2.jpg', 'rb')
        photo2 = open('photo/Avia 22-23.jpg', 'rb')
        photo3 = open('photo/VO 22-23.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=photo1)
        bot.send_photo(message.chat.id, photo=photo2)
        bot.send_photo(message.chat.id, photo=photo3)

    # вопросы про то, как найти клуб
    elif re.search(r'найти', text) is not None or \
            re.search(r'где.+клуб', text) is not None or \
            re.search(r'найти.+клуб', text) is not None or \
            re.search(r'какой.+адрес', text) is not None or \
            re.search(r'находит', text) is not None:
        photo1 = open('photo/Gasheka_how_to_find.png', 'rb')
        photo2 = open('photo/Avia_how_to_find.png', 'rb')
        photo3 = open('photo/VO_how_to_find.png', 'rb')
        bot.send_photo(message.chat.id, photo=photo1)
        bot.send_photo(message.chat.id, photo=photo2)
        bot.send_photo(message.chat.id, photo=photo3)

    # вопросы про то, как записаться в клуб, как подать заявку
    elif re.search('запис', text) is not None \
            or re.search('заявк', text) is not None \
            or text == '3':
        markup_reg = types.InlineKeyboardMarkup(row_width=1)
        btn_reg = types.InlineKeyboardButton('Запись на пробное',
                                             url='https://hirobots.spb.ru/probnoye')
        markup_reg.add(btn_reg)
        bot.send_message(message.chat.id, 'Перейдите в раздел сайта он-лайн записи, '
                                          'заполните поля и отправьте заявку:', reply_markup=markup_reg)

    # вопросы про то, какая стоимость, какая цена
    elif re.search(r'стои[т,м]', text) is not None or \
            re.search(r'цен[а,ы,е,у]', text) is not None or \
            text == '1':
        markup_price = types.InlineKeyboardMarkup(row_width=1)
        btn_price = types.InlineKeyboardButton('Стоимость и формы оплаты',
                                               url='https://hirobots.spb.ru/price')
        markup_price.add(btn_price)
        bot.send_message(message.chat.id, 'О стоимости абонементов'
                                          'можно узнать в разделе:', reply_markup=markup_price)
    # вопросы про то, как оплатить
    elif re.search(r'опла[т,ч]', text) is not None or \
            re.search(r'заплат', text) is not None or \
            text == '4':
        markup_price = types.InlineKeyboardMarkup(row_width=1)
        btn_price = types.InlineKeyboardButton('Способы оплаты',
                                               url='https://hirobots.spb.ru/pay')
        markup_price.add(btn_price)
        bot.send_message(message.chat.id, 'О способах оплаты '
                                          'можно узнать в разделе:', reply_markup=markup_price)


    # вопросы про бесплатное пробное занятие
    elif re.search(r'пробн', text) is not None or \
            re.search(r'попроб', text) is not None or \
            re.search(r'тестовое', text) is not None or \
            re.search(r'бесплатн', text) is not None or \
            text == '3':
        markup_test = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton('Бесплатное пробное занятие',
                                          url='https://hirobots.spb.ru/free-lesson')
        markup_test.add(btn4)
        bot.send_message(message.chat.id, 'Всем новичкам мы предлагаем бесплатное пробное занятие. '
                                          'Подробнее о пробном занятии, что взять с собой в разделе:',
                         reply_markup=markup_test)

    # вопросы про то, сколько раз в неделю надо посещать занятия
    elif re.search(r'раз в недел', text) is not None:
        bot.send_message(message.chat.id, 'Наши клубы рассчитаны на посещение 2 раза или 1 раз в неделю')

    # вопросы про то, можно ли ходить и платить разово, за одно занятие
    elif re.search(r'разово', text) is not None or re.search(r'одно\м*', message.text) is not None:
        bot.send_message(message.chat.id, 'В наших клубах абонементая система: 1 или 2 раза в неделю. '
                                          'Абонементы приобретаются на месяц. Можно ходить разово, '
                                          'но это получается дороже, и при этом место в группе не бронируется')

    # вопросы про то, со скольки лет можно приводить ребенка в клуб
    elif re.search(r'скольк[о,и] лет', text) is not None or re.search(r'како[го,м] возраст[а,е]',
                                                                      message.text) is not None:
        bot.send_message(message.chat.id, 'Мы принимаем детей от 5 до 12 лет. Бывает с 4 лет, но это решается '
                                          'индивидуально на пробном занятии')

    # вопросы про то, сколько детей в группах
    elif re.search(r'в групп[е,а]', text) is not None:
        bot.send_message(message.chat.id, 'В группах не более 7 детей')

    # вопросы про то, можно ли получить спавку для школы
    elif re.search(r'справк[у,а] для школ', text) is not None or \
            re.search(r'справк[у,а] в школ', text) is not None:
        bot.send_message(message.chat.id, 'Да, мы можем выдать справку о том, что Вы посещаете наш клуб'
                                          ' и по каким дням. Когда придете на занятие, скажите об этом тренеру')

    # вопросы про то, надо ли приносить сменку
    elif re.search(r'смен[н,к]', text) is not None:
        bot.send_message(message.chat.id, 'Пожалуйста, приносите на занятия сменную обувь! '
                                          'Это позволит сохранять клуб в чистоте.')

    # ответы по пунктам меню:
    elif text == '5':
        with open('Robo_5_12.txt', encoding='utf-8') as f:
            mess = f.read()
        bot.send_message(message.chat.id, mess)

    elif text == '6':
        with open('Robo_11_15.txt', encoding='utf-8') as f:
            mess = f.read()
        bot.send_message(message.chat.id, mess)

    elif text == '7':
        with open('3D_modelling.txt', encoding='utf-8') as f:
            mess = f.read()
        bot.send_message(message.chat.id, mess)

    elif text == '8':
        with open('Program.txt', encoding='utf-8') as f:
            mess = f.read()
        bot.send_message(message.chat.id, mess)

    # вопросы про контакты
    elif re.search(r'администра', text) is not None \
            or re.search(r'звонить', text) is not None \
            or re.search(r'связаться', text) is not None \
            or re.search(r'контакт', text) is not None \
            or re.search(r'телефон', text) is not None \
            or text == '9':
        markup_cont = types.InlineKeyboardMarkup(row_width=1)
        btn_price = types.InlineKeyboardButton('Контакты',
                                               url='https://hirobots.spb.ru/#97173d92-8711-4379-b9aa-653ecd552e9e')
        markup_cont.add(btn_price)
        bot.send_message(message.chat.id, 'Все наши контактные данные Вы можете '
                                          'найти в разделе:', reply_markup=markup_cont)
    # запрос погоды
    elif re.search(r'погода', text) is not None or text == '10':
        api_key = os.environ.get("YANDEX_API_KEY")
        y = YaWeather(api_key=api_key)
        res = y.forecast(Russia.SaintPetersburg)
        tr = Translator(from_lang='English', to_lang='Russian')  # объект класса Translator для перевода погоды с анг

        forecast = ''
        for f in res.forecasts:
            day = f.parts.day_short
            forecast += f'{f.date} | {day.temp} °C, {tr.translate(day.condition)}\n'

        bot.send_message(message.chat.id, f'Сейчас: {res.fact.temp} °C, ощущается как {res.fact.feels_like} °C \n'
                                          f'Погодные условия: {tr.translate(res.fact.condition)}')
        bot.send_message(message.chat.id, f'Погода на неделю:\n {forecast}')


    # во всех остальных случаях бот предлагает перейти в раздел контактов
    else:
        markup_oops = types.InlineKeyboardMarkup(row_width=1)
        btn_cont = types.InlineKeyboardButton('Контакты',
                                              url='https://hirobots.spb.ru/#97173d92-8711-4379-b9aa-653ecd552e9e')
        markup_oops.add(btn_cont)
        bot.send_message(message.chat.id, 'К сожалению, я не знаю ответ на этот вопрос! '
                                          'Попробуйте перефразировать вопрос или позвоните нам. '
                                          'Все контакты указаны в разделе:', reply_markup=markup_oops)


try:
    bot.polling(none_stop=True, interval=0)  # запускаем бесконечный цикл
except (requests.exceptions.ReadTimeout, telebot.apihelper.ApiException, telebot.apihelper.ApiTelegramException) as e:
    pass

if __name__ == '__main__':
    pass
