import telebot
#import gonfig
bot = telebot.TeleBot('######################')

@bot.message_handler(commands=['start',''])
def start_message(message):
#    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMFXv8_eG7QTGX7Ozi6pOaTObExVi8AAi4DAAK1cdoGqijNuZzJUrYaBA')
	 bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANiXwAB2oxCCUJkwTZR9dd8fDC3L__9AAI2BgACgD8HKFqM1bDy16FcGgQ')


@bot.message_handler(commands=['дуда'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здорова Дуда')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '':
        bot.send_message(message.chat.id, 'Я понимаю только только определенный список команд')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

#    elif message.text.lower() == 'some text':
 #       bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMFXv8_eG7QTGX7Ozi6pOaTObExVi8AAi4DAAK1cdoGqijNuZzJUrYaBA')

@bot.message_handler(content_types=['sticker'])       #gets sticker id 
def sticker_id(message):
    print(message)



# Обработчик команд '/start' и '/help'.
#@bot.message_handler(commands=['start', 'help'])
#def handle_start_help(message):
 #   pass

 # Обработчик для документов и аудиофайлов
#@bot.message_handler(content_types=['document', 'audio'])
#def handle_docs_audio(message):
 #   pass

 #Обработчик сообщений, подходящих под указанное регулярное выражение
#@bot.message_handler(regexp="SOME_REGEXP")
#def handle_message(message):
 #   pass

 # Обработчик сообщений, содержащих документ с mime_type 'text/plain' (обычный текст)
#@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
#def handle_text_doc(message):
 #   pass

if __name__ == '__main__':            #бесконечный цикл получения новых записей со стороны Telegram
    bot.polling(none_stop=True)    

