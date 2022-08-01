import telebot
import os
import re

from dotenv import load_dotenv
from telebot import types


load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'MENU'])
def start(message):
    hello_mess = f'Здравствуйте, {message.from_user.first_name}!\n' \
                 f'Я помощник навигации по сайту клубов HIROBOTS. ' \
           f'Задайте Ваш вопрос или напишите мне цифру, соответствующую интересующему Вас вопросу: \n'
    with open("menu_mess.txt", encoding="utf-8") as f:
        menu_mess = f.read()
    mess = hello_mess + menu_mess

    # bot.send_message(message.chat.id, message)

    markup_rkm = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_main_menu = types.KeyboardButton('/MENU')
    markup_rkm.add(btn_main_menu)

    bot.send_message(message.chat.id, mess, reply_markup=markup_rkm)


# @bot.message_handler(content_types='text')
# def get_user_text(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')


@bot.message_handler(content_types='text')
def got_text(message):
    text = message.text.lower() #получаем текст строчными буквами

    #вопросы про расписание занятий
    if re.search(r'расписани', text) is not None or text == '2':
        markup_shed = types.InlineKeyboardMarkup(row_width=1)
        btn_avia = types.InlineKeyboardButton('пр.Авиаконструкторов д.2',
                                          url='https://www.hirobots.spb.ru/raspisanie-kulba-aviakonstruktorov')
        btn_gash = types.InlineKeyboardButton('ул.Ярослава Гашека д.17',
                                          url='https://www.hirobots.spb.ru/raspisanie-kluba-gasheka')
        btn_vo = types.InlineKeyboardButton('Малый пр.В.О. д.88',
                                          url='https://www.hirobots.spb.ru/расписание-клуба-василеостровский')

        markup_shed.add(btn_avia, btn_gash, btn_vo)
        bot.send_message(message.chat.id, 'Выберите адрес клуба:', reply_markup=markup_shed)

    # вопросы про то, как найти клуб
    elif re.search(r'вас найти', text) is not None or \
            re.search(r'где.+клуб', text) is not None or\
            re.search(r'найти.+клуб', text) is not None:
        markup_shed = types.InlineKeyboardMarkup(row_width=1)
        btn_avia = types.InlineKeyboardButton('пр.Авиаконструкторов д.2',
                                          url='https://www.hirobots.spb.ru/raspisanie-kulba-aviakonstruktorov')
        btn_gash = types.InlineKeyboardButton('ул.Ярослава Гашека д.17',
                                          url='https://www.hirobots.spb.ru/raspisanie-kluba-gasheka')
        btn_vo = types.InlineKeyboardButton('Малый пр.В.О. д.88',
                                          url='https://www.hirobots.spb.ru/расписание-клуба-василеостровский')

        markup_shed.add(btn_avia, btn_gash, btn_vo)
        bot.send_message(message.chat.id, 'Какой клуб Вы ищете?:', reply_markup=markup_shed)

    # вопросы про то, как записаться в клуб, как подать заявку
    elif re.search('запис', text) is not None \
            or re.search('заявк', text) is not None \
            or text == '3':
        markup_reg = types.InlineKeyboardMarkup(row_width=1)
        btn_reg = types.InlineKeyboardButton('Запись на пробное',
                                          url='https://www.hirobots.spb.ru/services')
        markup_reg.add(btn_reg)
        bot.send_message(message.chat.id, 'Перейдите в раздел сайта он-лайн записи, '
                                          'заполните поля и отправьте заявку:', reply_markup=markup_reg)

    # вопросы про то, как оплатить, какая стоимость, какая цена
    elif re.search(r'опла[т,ч]', text) is not None or \
            re.search(r'заплат', text) is not None or \
            re.search(r'стои[т,м]', text) is not None or\
            re.search(r'цен[а,ы,е,у]', text) is not None or \
            text == '1' or \
            text == '4':
        markup_price = types.InlineKeyboardMarkup(row_width=1)
        btn_price = types.InlineKeyboardButton('Стоимость и формы оплаты',
                                          url='https://www.hirobots.spb.ru/stoimost')
        markup_price.add(btn_price)
        bot.send_message(message.chat.id, 'О стоимости абонементов и способах его оплаты '
                                          'можно узнать в разделе:', reply_markup=markup_price)

    # вопросы про бесплатное пробное занятие
    elif re.search(r'пробн', text) is not None or \
            re.search(r'попроб', text) is not None or \
            re.search(r'тестовое', text) is not None or \
            re.search(r'бесплатн', text) is not None or \
            text == '3':
        markup_test = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton('Бесплатное пробное занятие',
                                          url='https://www.hirobots.spb.ru/probnoye')
        markup_test.add(btn4)
        bot.send_message(message.chat.id, 'Всем новичкам мы предлагаем бесплатное пробное занятие. '
                                          'Подробнее о пробном занятии, что взять с собой в разделе:', reply_markup=markup_test)

    # вопросы про то, сколько раз в неделю надо посещать занятия
    elif re.search(r'раз в недел', text) is not None:
        bot.send_message(message.chat.id, 'Наши клубы рассчитаны на посещение 2 раза или 1 раз в неделю')

    # вопросы про то, можно ли ходить и платить разово, за одно занятие
    elif re.search(r'разово', text) is not None or re.search(r'одно\м*', message.text) is not None:
        bot.send_message(message.chat.id, 'В наших клубах абонементая система: 1 или 2 раза в неделю. '
                                          'Абонементы приобретаются на месяц. Можно ходить разово, '
                                          'но это получается дороже, и при этом место в группе не бронируется')

    # вопросы про то, со скольки лет можно приводить ребенка в клуб
    elif re.search(r'скольк[о,и] лет', text) is not None or re.search(r'како[го,м] возраст[а,е]', message.text) is not None:
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

    # вопросы про то, как с связаться, контакты администратора, номер телефона и пр.
    elif re.search(r'администра', text) is not None \
            or re.search(r'звонить', text) is not None \
            or re.search(r'связаться', text) is not None \
            or re.search(r'контакт', text) is not None \
            or re.search(r'телефон', text) is not None \
            or text == '9':
        markup_cont = types.InlineKeyboardMarkup(row_width=1)
        btn_price = types.InlineKeyboardButton('Контакты',
                                               url='https://www.hirobots.spb.ru/contact')
        markup_cont.add(btn_price)
        bot.send_message(message.chat.id, 'Все наши контактные данные Вы можете '
                                          'найти в разделе:', reply_markup=markup_cont)

    # во всех остальных случаях бот предлагает перейти в раздел контактов
    else:
        markup_oops = types.InlineKeyboardMarkup(row_width=1)
        btn_cont = types.InlineKeyboardButton('Контакты',
                                          url='https://www.hirobots.spb.ru/contact')
        markup_oops.add(btn_cont)
        bot.send_message(message.chat.id, 'К сожалению, я не знаю ответ на этот вопрос! '
                                          'Попробуйте спросить еще раз или позвоните нам. '
                                          'Все контакты указаны в разделе:', reply_markup=markup_oops)


# @bot.message_handler(commands=['help'])
# def menu(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     online_reg = types.KeyboardButton('Запись он-лайн', url='https://www.hirobots.spb.ru/services')
#     price = types.KeyboardButton('Стоимость и формы оплаты', url='https://www.hirobots.spb.ru/stoimost')
#     schedule = types.KeyboardButton('Расписание')
#
#     markup.add(online_reg, price)
#
#     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


# @bot.message_handler(regexp='стоимость')
# @bot.message_handler(regexp='сколько стоит')
# @bot.message_handler(regexp='цен')
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Стоимость абонементов', url='https://www.hirobots.spb.ru/stoimost'))
#     bot.send_message(message.chat.id, 'Перейдите в раздел сайта, чтобы ознакомится со стоимостью', reply_markup=markup)


bot.polling(none_stop=True)

if __name__ == '__main__':
    pass
