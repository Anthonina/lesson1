from telegram.ext import Updater, CommandHandler # Импорт необходимых компонентов

def start_bot(bot, update):
    hitext = '''Здравствуй! Рад общению!

Я простой бот и понимаю только команду /start
    '''
    update.message.reply_text(hitext)

def main():
    upd = Updater('356642084:AAF9SMmk9qMloEznZpzUSHCewe3kSWVYhv0') # Уникальный код, который выдаёт @BotFather
    
    upd.dispatcher.add_handler(CommandHandler('start', start_bot))
    
    upd.start_polling	# Подключаемся к платформе
    upd.idle()

if __name__ == '__main__': # Проверка. Если файл запустили напрямую, то функция отработает. Если файл куда-то импортировать и, например, использовать данный файл, так как в нём находятся какие-то функции, - при импорте часть вызова функции не отработает, и не возникнет ошибки.
    main()