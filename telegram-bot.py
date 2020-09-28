import telebot
print('Бот запущен!')
token = '1232053331:AAHIaDYeX2VHbMcHz0yqTe_HxR36_csn2nY'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Опять работать?!')

@bot.message_handler(content_types=['text'])
def send_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,'Здравствуйте!')
    elif message.text.lower() == 'как дела':
        bot.send_message(message.chat.id,'крутоооо, а у тебя как?')
    elif message.text.lower() == 'отлично':
        bot.send_message(message.chat.id,'так держать!')
    elif message.text.lower() == 'хорошо':
        bot.send_message(message.chat.id,'кто бы сомневался!')
    elif message.text.lower() == 'я вижу тебя':
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMWX3HkiGhvBPnh-1Fl-zI5BCraT2AAAvxeAAKezgsAAU0b95RBYosSGwQ')
    elif message.text.lower() == 'давай пообщаемся':
        bot.send_message(message.chat.id,'давай!чем ты увлекаешься?')
    elif message.text.lower() == 'программированием':
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMjX3HoymTQwLtyi-Q66XIaguxpvOMAAiAAA3j6-xfbmnEN8ra9AAEbBA')

@bot.message_handler(content_types= ['sticker'])
def send_sticker(message):
    print(message)


bot.polling()
