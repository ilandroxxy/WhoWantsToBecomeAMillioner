import random
import telebot
from telebot import types
import time

bot = telebot.TeleBot('5447726623:AAG_EYLjLIFqOz80fZHhZcBiMrVlylUdJcI')


# Users = {id: [[вопросы], кошелек]}
Users = {}
GIFT = [0, 100, 1000, 2000, 3000, 5000, 10000, 15000, 25000, 50000, 100000, 200000, 400000, 800000, 1500000, 3000000]
n = 15  # диапазон рандома вопросов

@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup()

    # region Оформляем кнопки que1-que15
    if call.data == 'que1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Юнг')
        btn2 = types.KeyboardButton('Гегель')
        btn3 = types.KeyboardButton('Ницше')
        btn4 = types.KeyboardButton('Шопенгауэр')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Кто из этих философов в 1864 году написал музыку на стихи А.С. Пушкина «Заклинание» и «Зимний вечер»?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Один')
        btn2 = types.KeyboardButton('Два')
        btn3 = types.KeyboardButton('Три')
        btn4 = types.KeyboardButton('Четыре')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Сколько раз в сутки подзаводят куранты Спасской башни Кремля?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Романист')
        btn2 = types.KeyboardButton('Драматург')
        btn3 = types.KeyboardButton('Поэт')
        btn4 = types.KeyboardButton('Эссеист')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Кто 1-м получил Нобелевскую премию по литературе?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)


    if call.data == 'que4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('М')
        btn2 = types.KeyboardButton('Н')
        btn3 = types.KeyboardButton('О')
        btn4 = types.KeyboardButton('П')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "С какой буквы начинаются слова, опубликованные в 16-м томе последнего издания Большой советской энциклопедии?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Фонвизин')
        btn2 = types.KeyboardButton('Державин')
        btn3 = types.KeyboardButton('Радищев')
        btn4 = types.KeyboardButton('Карамзин')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Кто из перечисленных был пажом во времена Екатерины II?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Гафний')
        btn2 = types.KeyboardButton('Кобальт')
        btn3 = types.KeyboardButton('Бериллий')
        btn4 = types.KeyboardButton('Теллур')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Какой химический элемент назван в честь злого подземного гнома?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Тбилиси')
        btn2 = types.KeyboardButton('Ереван')
        btn3 = types.KeyboardButton('Баку')
        btn4 = types.KeyboardButton('Минск')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "В какой из этих столиц бывших союзных республик раньше появилось метро?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que8':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('3')
        btn2 = types.KeyboardButton('4')
        btn3 = types.KeyboardButton('5')
        btn4 = types.KeyboardButton('6')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Сколько морей омывают Балканский полуостров?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que9':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Шея')
        btn2 = types.KeyboardButton('Уста')
        btn3 = types.KeyboardButton('Спина')
        btn4 = types.KeyboardButton('Палец')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Реки с каким названием нет на территории России?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que10':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Жнейка')
        btn2 = types.KeyboardButton('Шапка')
        btn3 = types.KeyboardButton('Болезнь')
        btn4 = types.KeyboardButton('Печка')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Что такое лобогрейка?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que11':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('«Предосторожность»')
        btn2 = types.KeyboardButton('«Пионеры»')
        btn3 = types.KeyboardButton('«Последний из могикан»')
        btn4 = types.KeyboardButton('«Зверобой»')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Какой роман Фенимор Купер написал на спор с женой?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que12':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Кирасиры')
        btn2 = types.KeyboardButton('Уланы')
        btn3 = types.KeyboardButton('Драгуны')
        btn4 = types.KeyboardButton('Гусары')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Какой вид кавалерии предназначался для боевых действий как в конном, так и в пешем строю?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que13':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Валентин')
        btn2 = types.KeyboardButton('Евгений')
        btn3 = types.KeyboardButton('Георгий ')
        btn4 = types.KeyboardButton('Виктор')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Какое имя не принимал ни один папа римский?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que14':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Висбаден')
        btn2 = types.KeyboardButton('Цербст')
        btn3 = types.KeyboardButton('Штеттин ')
        btn4 = types.KeyboardButton('Дармштадт')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "В каком немецком городе родилась будущая императрица России Екатерина II?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)

    if call.data == 'que15':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Точить лясы')
        btn2 = types.KeyboardButton('Бить баклуши')
        btn3 = types.KeyboardButton('Пускать пыль в глаза ')
        btn4 = types.KeyboardButton('Переливать из пустого в порожнее')
        markup.add(btn1, btn2, btn3, btn4)
        message_text = "Что запрещал указ, который в 1726 году подписала Екатерина I?"
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup)
    # endregion que1-15


@bot.message_handler(commands=['start'])
def start(message):
    Users[message.chat.id] = [[], 0]
    print(Users[message.chat.id])
    while True:
        temp = random.randint(1, n)
        if temp not in Users[message.chat.id][0]:
            Users[message.chat.id][0].append(temp)
            print(Users[message.chat.id])
            break
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Начать игру", callback_data='que' + str(temp)))
    bot.send_message(message.chat.id, 'Добро пожаловать в игру\n *"Кто хочет стать миллионером"!*', parse_mode='Markdown', reply_markup=markup)


# region Команды: show_list, show
@bot.message_handler(commands=['show_list'])
def show_list(message):
    if message.chat.id == 811476623 or message.chat.id == 1891281816:
        message_text = 'Вопросы на которые вы ответили правильно: '
        Temp = Users[message.chat.id][0][:-1]
        Temp.sort()
        for i in range(0, len(Temp)):
            message_text += str(Temp[i]) + ', '
        message_text = message_text[:-2]
        bot.send_message(message.chat.id, message_text)
    else:
        bot.send_message(message.chat.id, 'Вы не можете использовать эту функцию')


@bot.message_handler(commands=['show'])
def show(message):
    bot.send_message(message.chat.id, f'*Промежуточные результаты:*\nКоличество правильных ответов: {len(Users[message.chat.id][0])-1}\nКоличество оставшихся вопросов: {16-len(Users[message.chat.id][0])}', parse_mode='Markdown')
# endregion Команды: show_list, show

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()

    if get_message_bot == 'Начать заново':
        while True:
            temp = random.randint(1, n)
            if temp not in Users[message.chat.id][0]:
                Users[message.chat.id][0].append(temp)
                break
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Следующий вопрос", callback_data='que' + str(temp)))
        bot.send_message(message.chat.id, "Запустите игру заново нажатием клавиши:", reply_markup=markup)



    elif get_message_bot == 'Заглянуть в кошелёк':
        bot.send_message(message.chat.id, f"Денег в вашем кошельке: {Users[message.chat.id][1]}")



    elif get_message_bot == 'Забрать выигрыш':
        if len(Users[message.chat.id][0]) == n:
            balance = GIFT[len(Users[message.chat.id][0])]
        else:
            balance = GIFT[len(Users[message.chat.id][0])-1]
        Users[message.chat.id][1] += balance
        Users[message.chat.id][0].clear()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f"Новое значение денег в вашем кошельке: {Users[message.chat.id][1]}, а выйгрыш обнулился!", reply_markup=markup)




    # region Обработка правильных и неправильных ответов que1-que15
    elif get_message_bot in ('Ницше', 'Два', 'Поэт', 'М', 'Радищев', 'Кобальт', 'Тбилиси', 'Спина', '6', 'Жнейка', 'Виктор', 'Гусары', 'Переливать из пустого в порожнее', 'Дармштадт', '«Предосторожность»'):
        balance = GIFT[len(Users[message.chat.id][0])]  # В списке Balance, на 0 позиции будет храниться кол-во очков заработанных на данный момент игры
        while True:
            temp = random.randint(1, n)
            if len(Users[message.chat.id][0]) == n:
                bot.send_message(message.chat.id, "Поздравляем, Вы ответили на все вопросы нашей игры 🎯")
                break
            elif temp not in Users[message.chat.id][0]:
                Users[message.chat.id][0].append(temp)
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(types.InlineKeyboardButton("Следующий вопрос", callback_data='que' + str(temp)))
                bot.send_message(message.chat.id, f"Правильный ответ", reply_markup=markup)
                break


        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup3.add(types.KeyboardButton("Заглянуть в кошелёк"), types.KeyboardButton("Забрать выигрыш"))
        bot.send_message(message.chat.id, f'Ваш выигрыш: {balance} рублей', reply_markup=markup3)

    # que1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Юнг':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))   # Генерим кнопку для перезапуска игры
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)  # А тут просто в одну строку выводи кол-во денег: Список[кол-во ответов]

    elif get_message_bot == 'Гегель':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Шопенгауэр':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que1 ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Один':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Четыре':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Три':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que2 ----------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que3 ----------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Романист':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Драматург':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Эссеист':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que3 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que4 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Н':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'О':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'П':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que4 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que5 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Карамзин':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Державин':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Фонвизин':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que5 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que6 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Гафний':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Бериллий':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    elif get_message_bot == 'Теллур':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que6 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que7 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Ереван':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Баку':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Минск':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que7 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que8 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == '3':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '4':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '5':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que8 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que8 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Шея':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Уста':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Палец':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que9 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que10 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Шапка':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Болезнь':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[len(QUE)]} рублей', reply_markup=markup)

    elif get_message_bot == 'Печка':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que10 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que11 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == '«Пионеры»':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '«Последний из могикан»':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == '«Зверобой»':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que11 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que12 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Драгуны':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Уланы':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Кирасиры':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que12 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que13 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Валентин':
        Users[message.chat.id] = []
        l = len(Users[message.chat.id])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Евгений':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Георгий':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que13 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que14 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Висбаден':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Цербст':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Штеттин':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que14 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    # que15 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif get_message_bot == 'Точить лясы':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Бить баклуши':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)

    elif get_message_bot == 'Пускать пыль в глаза':
        Users[message.chat.id][0] = []
        l = len(Users[message.chat.id][0])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
        markup.add(types.KeyboardButton("Начать заново"))
        bot.send_message(message.chat.id, f'Вы проиграли:(\nВаш выигрыш: {GIFT[l]} рублей', reply_markup=markup)
    # que15 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    # endregion Обработка правильных и неправильных ответов que1-que15

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)