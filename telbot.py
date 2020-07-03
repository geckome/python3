import telebot

bot = telebot.TeleBot('974588367:AAFy00TzVqRiwaRLtx_l3kRkK41M2wkGtBc')

@bot.message_handler(commands=['start',''])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет это тестовый бот')


@bot.message_handler(commands=['blabla'])
def start_message(message):
    bot.send_message(message.chat.id, 'здорова ')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

#    elif message.text.lower() == 'huy':
 #       bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMFXv8_eG7QTGX7Ozi6pOaTObExVi8AAi4DAAK1cdoGqijNuZzJUrYaBA')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
