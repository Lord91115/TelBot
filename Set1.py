import telebot

bot = telebot.TeleBot('1245145219:AAF4XnIZxtAFjyHaqf8hQE9qOrbTirTFZ7g')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет','Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Ну начнём /start',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет, мой друг')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорой встречи')
    elif message.text.lower() == 'ок':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBP18iHoxYwRiYTKgmrT5wtkN72qNeAAJWAANBtVYM1ZNlBU-tNFYaBA')


@bot.message_handler(content_types=['sticker'])
def send_text(message):
    print(message)


#@bot.message_handler(content_types=['photo'])
#def photo_send(message):
 #   print(message)


bot.polling()