import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)



bot.polling(none_stop=True)