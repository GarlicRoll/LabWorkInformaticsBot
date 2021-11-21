# graphic interface for lab work (telegram/extraversion)
import telebot
import os
import compiler, decompiler

def init_bot(): # инициализация бота
    print("Bot_init")
    
    telegram_token = os.environ.get('TOKEN')
    '''
    # для лоакального тестирования
    global bot
    bot = telebot.TeleBot("")
    '''

# стандартная процедура для запуска приложения
if __name__ == "__main__":
    bot = None 
    init_bot() 
    print("Start")

# стартовое сообщение
@bot.message_handler(commands=['test', 'start']) # при командах /test и /start
def statistic_command(message):
    bot.send_message(message.chat.id, 'Enter the word/number in fibonacci system!')

# реакция на отправку ему текстового сообщения
@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        number = message.text
        print(compiler.main(number))
        print(decompiler.main(number))
        bot.send_message(message.chat.id, compiler.main(number)) # из чего-то в число
        bot.send_message(message.chat.id, decompiler.main(number)) # из числа во что-то
    except:
        bot.send_message(message.chat.id, "Something went wrong...")

bot.polling()