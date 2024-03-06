"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging, ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй")


# def find_const(update, context):
#    text = update.message.text.split(" ")
#    planet_name = 'Arcturus'
#    planet = ephem.star(planet_name)
#    const = ephem.constellation(planet)
#    print(const)
#    print(text[1])

def find_const(update, context):
    planet_name = update.message.text.split()[1]
    mars = ephem.Mars('2024/02/19')
    const = ephem.constellation(mars)
    if planet_name == 'Mars':
        update.message.reply_text(const)

def main():
    mybot = Updater("6849800937:AAHXrA00ZD0rY-0ZUMmTFDyRkXckQGBLWaI", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_const))

    logging.info("Бот стартовал")
    mybot.start_polling()

if __name__ == "__main__":
    main()
