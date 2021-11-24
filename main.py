# graphic interface for lab work (telegram/extraversion)
import telebot
import os

import compiler, decompiler
import time

def init_bot(): # инициализация бота
    print("Bot_init")
    
    global bot
    
    telegram_token = os.environ.get('TOKEN')
    bot = telebot.TeleBot(telegram_token)
    '''

    # для лоакального тестирования
    bot = telebot.TeleBot("")
    '''
def launching():
    global chat_id
    global main_bot_message_id
    global first_message
    path = 'images\launching\op'
    for id in range(1, 25 + 1):
        try:
            if not first_message:
                bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + str(id) + '-min.png', 'rb')))
                time.sleep(0.2)
        except:
            pass

def make_arrows():
    KeyboardMarkup = telebot.types.InlineKeyboardMarkup()
    KeyboardMarkup.add(telebot.types.InlineKeyboardButton("⬆️", callback_data = "up"), telebot.types.InlineKeyboardButton("⬇️", callback_data = "down"), telebot.types.InlineKeyboardButton("🆗", callback_data = "ok"))
    return KeyboardMarkup

# стандартная процедура для запуска приложения
if __name__ == "__main__":
    bot = None
    chat_id = None
    main_bot_message_id = None
    main_user_message_id = None
    init_bot()
    print("Start")

# стартовое сообщение
@bot.message_handler(commands=['test', 'start']) # при командах /test и /start
def statistic_command(message):
    global main_bot_message_id
    global main_user_message_id
    global first_message
    global chat_id
    global menu_option
    try:
        bot.delete_message(chat_id, main_bot_message_id)
    except:
        pass
    first_message = True
    menu_option = 1
    if first_message:
        chat_id = message.chat.id
        main_bot_message_id = bot.send_photo(message.chat.id, photo=open('images\logo.png', 'rb'), caption='Press any key to boot the system: |').message_id
        bot.delete_message(message.chat.id, message.id)
    #message_id_my = bot.send_photo(message.chat.id, photo=open('lab_work_informatics_bot\images\game_over.jpg', 'rb')).message_id
    #time.sleep(1)
    #bot.edit_message_media(chat_id=message.chat.id, message_id=message_id_my, media=telebot.types.InputMediaPhoto(open('lab_work_informatics_bot\images\dnevnikru.jpg', 'rb')))
    while first_message:
        time.sleep(0.5)
        if first_message:bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\logo.png', 'rb'), caption = 'Press any key to boot the system:'))
        #if first_message: bot.edit_message_text('Press any key to boot the system:', message.chat.id, main_bot_message_id)
        time.sleep(0.5)
        if first_message:bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\logo.png', 'rb'), caption = 'Press any key to boot the system: |'))
        #if first_message: bot.edit_message_text('Press any key to boot the system: |', message.chat.id, main_bot_message_id)

# реакция на отправку ему текстового сообщения
@bot.message_handler(content_types=['text'])
def handle_text(message):
    global main_user_message_id
    global main_bot_message_id
    global first_message
    
    if first_message:
        main_user_message_id = message.id
        first_message = False
        bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\logo.png', 'rb'), caption = 'System launched'))
        #bot.edit_message_text(message.text, message.chat.id, main_user_message_id)
        bot.delete_message(message.chat.id, message.id)
        arrows = make_arrows()
        bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\mainmenu1.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
    else:
        try:
            bot.delete_message(message.char.id, message.id)
            number = message.text
            print(compiler.main(number))
            print(decompiler.main(number))
            bot.send_message(message.chat.id, compiler.main(number)) # из чего-то в число
            bot.send_message(message.chat.id, decompiler.main(number)) # из числа во что-то
        except:
            bot.send_message(message.chat.id, "Something went wrong...")

@bot.callback_query_handler(lambda callback: callback.data) # отклик на нажатие оценки
def push_button(callback):
    global menu_option
    global chat_id
    global main_bot_message_id
    global first_message

    arrows = make_arrows()
    if callback.data == "up":
        if menu_option == 1: menu_option = 3; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\mainmenu3.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 2: menu_option = 1; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\mainmenu1.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 3: menu_option = 2; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        
    elif callback.data == "down":
        if menu_option == 1: menu_option = 2; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 2: menu_option = 3; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\mainmenu3.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 3: menu_option = 1; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open('images\mainmenu1.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)

    elif callback.data == "ok":
        if menu_option == 1: launching()
        elif menu_option == 2: pass
        elif menu_option == 3: bot.delete_message(chat_id, main_bot_message_id)
    
bot.polling()