import requests
import telebot


bot = telebot.TeleBot('5507916843:AAGuT6H1Ux7iHDpGJSEPZmdGrnI9MbsTFFg')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} введи название города'
    bot.send_message(message.chat.id, mess)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    try:
        bot.send_message(message.chat.id, what_weather(message.text))
    except:
        bot.send_message(message.chat.id, 'Не знаю такого города')


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text

bot.polling(none_stop=True)