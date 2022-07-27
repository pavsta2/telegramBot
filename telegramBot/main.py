import telebot
import os
import re

from dotenv import load_dotenv
from telebot import types

load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте,{message.from_user.first_name}, я помощник навигации по сайту клубов HIROBOTS. ' \
           f'Задайте Ваш вопрос или перейдите в интересующий раздел сайта, выбрав кнопку меню ниже'
    # bot.send_message(message.chat.id, message)

    markup_rkm = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_online_reg = types.KeyboardButton('Запись на пробное')
    btn_price = types.KeyboardButton('Стоимость и формы оплаты')
    btn_schedule = types.KeyboardButton('Расписание')
    markup_rkm.add(btn_online_reg, btn_price, btn_schedule)

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
    if re.search(r'[Р,р]асписани', message.text) is not None:
        markup_shed = types.InlineKeyboardMarkup(row_width=1)
        btn_avia = types.InlineKeyboardButton('пр.Авиаконструкторов д.2',
                                          url='https://www.hirobots.spb.ru/raspisanie-kulba-aviakonstruktorov')
        btn_gash = types.InlineKeyboardButton('ул.Ярослава Гашека д.17',
                                          url='https://www.hirobots.spb.ru/raspisanie-kluba-gasheka')
        btn_vo = types.InlineKeyboardButton('Малый пр.В.О. д.88',
                                          url='https://www.hirobots.spb.ru/расписание-клуба-василеостровский')

        markup_shed.add(btn_avia, btn_gash, btn_vo)
        bot.send_message(message.chat.id, 'Выберите адрес клуба:', reply_markup=markup_shed)

    elif re.search('[З,з]апис', message.text) is not None:
        markup_reg = types.InlineKeyboardMarkup(row_width=1)
        btn_reg = types.InlineKeyboardButton('Запись на пробное',
                                          url='https://www.hirobots.spb.ru/services')
        markup_reg.add(btn_reg)
        bot.send_message(message.chat.id, 'Перейдите в раздел сайта он-лайн записи, '
                                          'заполните поля и отправьте заявку:', reply_markup=markup_reg)

    elif re.search(r'[О,о]пла[т,ч]', message.text) is not None or \
            re.search(r'[З,з]аплат', message.text) is not None or \
            re.search(r'[С,с]тоит', message.text) is not None:
        markup_reg = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton('Стоимость и формы оплаты',
                                          url='https://www.hirobots.spb.ru/stoimost')
        markup_reg.add(btn4)
        bot.send_message(message.chat.id, 'Перейдите в раздел сайта и ознакомьтесь со стоимостью абонементов'
                                          ' и формах оплаты:', reply_markup=markup_reg)

    elif re.search(r'[П,п]робн', message.text) is not None or \
            re.search(r'[П,п]опроб', message.text) is not None or \
            re.search(r'[Т,т]естовое', message.text) is not None or \
            re.search(r'[Б,б]есплатн', message.text) is not None:
        markup_test = types.InlineKeyboardMarkup(row_width=1)
        btn4 = types.InlineKeyboardButton('Бесплатное пробное занятие',
                                          url='https://www.hirobots.spb.ru/probnoye')
        markup_test.add(btn4)
        bot.send_message(message.chat.id, 'Всем новичкам мы предлагаем бесплатное пробное занятие. '
                                          'Подробнее в разделе:', reply_markup=markup_test)

    elif re.search(r'раз в недел', message.text) is not None:
        bot.send_message(message.chat.id, 'Наши клубы рассчитаны на посещение 2 раза или 1 раз в неделю')

    elif re.search(r'разово', message.text) is not None or re.search(r'одно\м*', message.text) is not None:
        bot.send_message(message.chat.id, 'В наших клубах абонементая система: 1 или 2 раза в неделю. '
                                          'Абонементы приобретаются на месяц. Можно ходить разово, '
                                          'но это получается дороже, и при этом место в группе не бронируется')

    elif re.search(r'скольк[о,и] лет', message.text) is not None or re.search(r'года', message.text) is not None:
        bot.send_message(message.chat.id, 'Мы принимаем детей от 5 до 12 лет. Бывает с 4 лет, но это решается '
                                          'индивидуально на пробном занятии')

    elif re.search(r'в групп[е,а]', message.text) is not None:
        bot.send_message(message.chat.id, 'В группах не более 7 детей')
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
