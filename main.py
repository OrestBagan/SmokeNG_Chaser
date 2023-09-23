import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

tovar_list = ['✅Вишня 50 MG (10мл)', '✅Полуниця банан 50 MG (10мл)', '✅Балі тріпл шот 50 MG (10мл)', '✅Полнуниця 50 MG (10мл)', '✅Кола 50 MG (10мл)', '✅Ягоди ICE 50 MG (10мл)', '❌Ожиновий джем', "❌М'ята", '❌Персик ICE', '❌Блакитна малина-лимонад']
tovar = ''
for i in tovar_list:
    tovar += i + '\n'
text = '🔥 В наявності (Chaser)🔥\n\nChaser(salt nic.)\nЦіна 🔥: 1️⃣1️⃣0️⃣грн\n\n'


@bot.message_handler(commands=['start'])
def start(message):
    sti = open('img/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.InlineKeyboardButton('Зробити замовлення')

    murkup.add(button)

    bot.send_message(message.chat.id, 'Вітаємо у телеграм боті <b><i>{1.first_name}</i></b>\nЦей бот створений для оформлення замовленя у нашому магазині'.format(message.from_user, bot.get_me()), parse_mode=('html'), reply_markup=murkup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.chat.type == 'private':
        if message.text == 'Зробити замовлення':
            ph1 = open('img/photo_one.webp', 'rb')
            bot.send_sticker(message.chat.id, ph1)
            bot.send_message(message.chat.id, text + tovar)

bot.polling(none_stop=True)