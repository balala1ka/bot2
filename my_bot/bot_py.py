from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    balala1ka_bot = Updater('1052455624:AAE7myxeycBT4U0ojhiz52O0d-Pj1YFExFU', request_kwargs=PROXY)
    dp = balala1ka_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    balala1ka_bot.start_polling()
    balala1ka_bot.idle()


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def greet_user(bot, update):
    print('Вызван /start')
    print('Ну я запустился епт!')
    update.message.reply_text('Здарова епта')


main()
greet_user()
