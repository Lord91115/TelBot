import telebot

bot = telebot.TeleBot('1245145219:AAF4XnIZxtAFjyHaqf8hQE9qOrbTirTFZ7g')



@bot.message_handler(content_types=['photo'])
def photo_send(message):
    print(message)
#'photo': [<telebot.types.PhotoSize object at 0x02E555E0>, <telebot.types.PhotoSize object at 0x02E55F40>, <telebot.types.PhotoSize object at 0x02E555F8>]




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет, мой друг')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорой встречи')
    elif message.text.lower() == 'ок':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBP18iHoxYwRiYTKgmrT5wtkN72qNeAAJWAANBtVYM1ZNlBU-tNFYaBA')
    elif message.text.lower() =='photo':
        bot.send_photo(photo='[<telebot.types.PhotoSize object at 0x02E555E0>, <telebot.types.PhotoSize object at 0x02E55F40>, <telebot.types.PhotoSize object at 0x02E555F8>]')

        #elif message.text.lower() == 'photo':
        bot.send_photo(id, photo='[<telebot.types.PhotoSize object at 0x02E555E0>]')


        bot