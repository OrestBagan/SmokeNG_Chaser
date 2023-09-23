import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sti = open('img/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    murkup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Ні якую', callback_data='no')
    button2 = types.InlineKeyboardButton('Так звичайно', callback_data='yes')

    murkup.add(button1, button2)

    bot.send_message(message.chat.id, 'Вітаємо у нашому магазині, бажаєте зробити замовлення?', reply_markup=murkup)

bot.polling(none_stop=True)