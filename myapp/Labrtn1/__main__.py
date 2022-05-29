import telebot
from telebot import types
Token = '5383700902:AAGpCS8KEL11_PHKmOoroHMWJBeU2dJKaSY'
bot = telebot.TeleBot(token=Token)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "Hello":
        knopka = telebot.types.InlineKeyboardMarkup()
        knopka.add(telebot.types.InlineKeyboardButton(text='Понедельник', callback_data='Понедельник'))
        knopka.add(telebot.types.InlineKeyboardButton(text='Вторник', callback_data='Вторник'))
        knopka.add(telebot.types.InlineKeyboardButton(text='Среда', callback_data='Среда'))
        knopka.add(telebot.types.InlineKeyboardButton(text='Четверг', callback_data='Четверг'))
        knopka.add(telebot.types.InlineKeyboardButton(text='Пятница', callback_data='Среда'))
        knopka.add(telebot.types.InlineKeyboardButton(text='Суббота', callback_data='Суббота'))
        knopka.add(telebot.types.InlineKeyboardButton(text='Воскресенье', callback_data='Воскресенье'))
        bot.send_message(message.chat.id, text="Какой у Вас сегодня день?", reply_markup=knopka)
    else:
        bot.send_message(message.from_user.id, text="Если хочешь получить шутку про сегодняшний день, то я жду слово: \n                                      Hello")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Понедельник":
        bot.send_photo(call.message.chat.id, 'http://img2.reactor.cc/pics/post/анекдоты-анекдоты-про-наркоманов-и-алкоголиков-300473.jpeg')
    elif call.data == "Вторник":
        bot.send_photo(call.message.chat.id,'https://r2.mt.ru/r15/photo0E5A/20873024362-0/jpg/bp.jpeg')
    elif call.data == "Среда":
            bot.send_photo(call.message.chat.id,'https://pbs.twimg.com/media/C-7NszzWAAAcU8Z.jpg')
    elif call.data == "Четверг":
            bot.send_photo(call.message.chat.id,'http://risovach.ru/upload/2013/09/mem/don-vito-korleone_30121841_orig_.jpeg')
    elif call.data == "Пятница":
            bot.send_photo(call.message.chat.id,'http://img2.joyreactor.cc/pics/post/анекдоты-анекдоты-про-наркоманов-и-алкоголиков-296442.jpeg')
    elif call.data == "Суббота":
            bot.send_photo(call.message.chat.id,'https://megapozitiv.com/wp-content/uploads/2019/06/28-4.jpg')
    elif call.data == "Воскресенье":
            bot.send_photo(call.message.chat.id,'https://i05.fotocdn.net/s107/6379bf6d67e14f7e/public_pin_l/2325223044.jpg')
    bot.send_message(call.message.chat.id)
if __name__ == '__main__':
    main()
bot.polling(none_stop=True, interval=0)