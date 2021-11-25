# graphic interface for lab work (telegram/extraversion)
import telebot
import os

import compiler, decompiler
from eight_to_ten import eight_to_ten
from morze import morse
from three_to_eight import three_to_eight
import time

def level_1():
    global password
    global is_level_1
    is_level_1 = True
    if difficulty == 1: password = "Hi"
    elif difficulty == 2: password = "Hello"
    elif difficulty == 3: password = "Good morning"
    encrypted_password = compiler.main(password)
    bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Hack the terminal:(fib>10)\nEncrypted password: ' + encrypted_password))

def level_2(word):
    global password
    global is_level_2
    global is_level_1
    is_level_1 = False
    is_level_2 = True
    bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Hack the terminal (10>8):\nEncrypted password: ' + word))

def level_3(word):
    global password
    global is_level_3
    global is_level_2
    is_level_2 = False
    is_level_3 = True
    bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Hack the terminal (8>morze):\nEncrypted password: ' + word))

def level_4(word):
    global password
    global is_level_4
    global is_level_3
    is_level_3 = False
    is_level_4 = True
    bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Hack the terminal (morze>word):\nEncrypted password: ' + word))

def init_bot(): # инициализация бота
    print("Bot_init")
    
    global bot
    
    telegram_token = os.environ.get('TOKEN')
    bot = telebot.TeleBot(telegram_token)
    
    '''
    
    # для локального тестирования
    bot = telebot.TeleBot("")
    '''
def launching():
    global chat_id
    global main_bot_message_id
    global first_message
    folder = 'launching\op'
    for id in range(1, 25 + 1):
        try:
            if not first_message:
                bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + folder +  str(id) + '-min.png', 'rb')))
                time.sleep(0.2)
        except:
            pass

def make_arrows():
    KeyboardMarkup = telebot.types.InlineKeyboardMarkup()
    KeyboardMarkup.add(telebot.types.InlineKeyboardButton("⬆️", callback_data = "up"), telebot.types.InlineKeyboardButton("⬇️", callback_data = "down"), telebot.types.InlineKeyboardButton("🆗", callback_data = "ok"))
    return KeyboardMarkup

def make_difficulties():
    KeyboardMarkup = telebot.types.InlineKeyboardMarkup()
    KeyboardMarkup.add(telebot.types.InlineKeyboardButton("1", callback_data = "1"), telebot.types.InlineKeyboardButton("2", callback_data = "2"), telebot.types.InlineKeyboardButton("3", callback_data = "3"))
    return KeyboardMarkup
# стандартная процедура для запуска приложения
if __name__ == "__main__":
    bot = None
    chat_id = None
    main_bot_message_id = None
    main_user_message_id = None
    difficulty = 2
    attempts = 0
    path = "images\\"
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
    global is_level_1
    global is_level_2
    global is_level_3
    global is_level_4
    try:
        bot.delete_message(chat_id, main_bot_message_id)
    except:
        pass
    is_level_1 = False
    is_level_2 = False
    is_level_3 = False
    is_level_4 = False
    first_message = True
    menu_option = 1
    if first_message:
        chat_id = message.chat.id
        main_bot_message_id = bot.send_photo(message.chat.id, photo=open(path + 'logo.png', 'rb'), caption='Press any key to boot the system: |').message_id
        bot.delete_message(message.chat.id, message.id)
    while first_message:
        time.sleep(0.5)
        if first_message:bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'logo.png', 'rb'), caption = 'Press any key to boot the system:'))
        time.sleep(0.5)
        if first_message:bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'logo.png', 'rb'), caption = 'Press any key to boot the system: |'))

# реакция на отправку ему текстового сообщения
@bot.message_handler(content_types=['text'])
def handle_text(message):
    global main_user_message_id
    global main_bot_message_id
    global first_message
    global attempts
    global password

    if first_message:
        main_user_message_id = message.id
        first_message = False
        bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'logo.png', 'rb'), caption = 'System launched'))
        bot.delete_message(message.chat.id, message.id)
        arrows = make_arrows()
        bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu1.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
    elif is_level_1:
        try:
            bot.delete_message(chat_id, message.id)
            word = message.text
            if word == str(eight_to_ten(three_to_eight(morse(password)[0])[0])[0]):
                bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Termianl hacked! Warning! Second layer of defense!\n'))
                time.sleep(2)
                level_2(word)
            else:
                attempts += 1
        except:
            bot.send_message(message.chat.id, "Something went wrong...")
    elif is_level_2:
        try:
            bot.delete_message(chat_id, message.id)
            word = message.text
            if word == str(three_to_eight(morse(password)[0])[0]):
                bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Termianl hacked! Warning! Second layer of defense!\n'))
                time.sleep(2)
                level_3(word)
            else:
                attempts += 1
        except:
            bot.send_message(message.chat.id, "Something went wrong...")
    elif is_level_3:
        try:
            bot.delete_message(chat_id, message.id)
            word = message.text
            if word == str(morse(password)[0]):
                bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Termianl hacked! Warning! Last layer of defense!\n'))
                time.sleep(2)
                level_4(word)
            else:
                attempts += 1
        except:
            bot.send_message(message.chat.id, "Something went wrong...")
    elif is_level_4:
        try:
            bot.delete_message(chat_id, message.id)
            word = message.text
            if word == password:
                bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'dnevnikru.jpg', 'rb'), caption = 'Termianl hacked!'))
            else:
                attempts += 1
        except:
            bot.send_message(message.chat.id, "Something went wrong...")

@bot.callback_query_handler(lambda callback: callback.data) # отклик на нажатие встроенной в сообщение кнопки
def push_button(callback):
    global menu_option
    global chat_id
    global main_bot_message_id
    global first_message
    global gaming_process

    arrows = make_arrows()
    if callback.data == "up":
        if menu_option == 1: menu_option = 3; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu3.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 2: menu_option = 1; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu1.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 3: menu_option = 2; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        
    elif callback.data == "down":
        if menu_option == 1: menu_option = 2; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 2: menu_option = 3; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path +'mainmenu3.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
        elif menu_option == 3: menu_option = 1; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu1.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)

    elif callback.data == "ok":
        if menu_option == 1:
            launching()
            level_1()
        elif menu_option == 2:
            difficulties = make_difficulties()
            bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=difficulties)
        elif menu_option == 3: bot.delete_message(chat_id, main_bot_message_id)
    
    elif callback.data == "1": difficulty = 1; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
    elif callback.data == "2": difficulty = 2; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)
    elif callback.data == "3": difficulty = 3; bot.edit_message_media(chat_id=chat_id, message_id=main_bot_message_id, media=telebot.types.InputMediaPhoto(open(path + 'mainmenu2.png', 'rb'), caption = 'Choose the option:'), reply_markup=arrows)

bot.polling()