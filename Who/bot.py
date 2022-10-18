import telebot
from telebot import types
from telebot import callback_data
import sqlite3
import emoji

bot = telebot.TeleBot('Your Token')

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    if call.data == 'КлючСобытия':

@bot.message_handler(commands=['start'])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('Репетитор')
    markup1.add(btn1)
    send_mess = f'👋 Доброго времени суток, *{message.from_user.first_name}*!'
    bot.send_message(message.chat.id, send_mess, parse_mode='Markdown', reply_markup=markup1)

    markup2 = types.InlineKeyboardMarkup(row_width=1)
    markup2.add(types.InlineKeyboardButton("Кнопка", callback_data="КлючСобытия"))
    pic_1 = open("hello.jpeg", 'rb')
    bot.send_photo(message.chat.id, pic_1, reply_markup=markup2)

@bot.message_handler(commands=['voice'])
def voice(message):

    @bot.message_handler(content_types=['text'])
    def message_input(message):
        text_message = message.text
        bot.send_message(message.chat.id, text_message)

    bot.register_next_step_handler(message, message_input)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == "Репетитор":

bot.polling(none_stop=True)