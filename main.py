# @Qiamast
import logging
import sys
import time

import telebot
from telebot import types

API_TOKEN = 'i dont love to paste my bot token here for public repo :)'

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)


@bot.inline_handler(lambda query: query.query == 'help')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'نتیجه اولی که با api کال نشده', types.InputTextMessageContent('رفیق هنوز زوده واسه کار'))
        r2 = types.InlineQueryResultArticle('2', 'نتیجه دوم', types.InputTextMessageContent('سلام مثل اینکه حالت خوش نیست گزینه دوم انتخاب کردی'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == 'pic')
def query_photo(inline_query):
    try:
        r = types.InlineQueryResultPhoto('1',
                                         'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Lana_Rhoades_cropped.jpg/820px-Lana_Rhoades_cropped.jpg',
                                         input_message_content=types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultPhoto('2',
                                          'https://i.pinimg.com/736x/62/a8/a3/62a8a32e09822d647e12387b8f5d907c.jpg')
        bot.answer_inline_query(inline_query.id, [r, r2], cache_time=1)
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'I am developing :) ', types.InputTextMessageContent('Hey my name is Imarch :.:.:'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
