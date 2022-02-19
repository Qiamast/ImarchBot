import logging
import sys
import time

import telebot
from telebot import types

API_TOKEN = 'Paste Bot Token Here!'

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result1', types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('hi'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == 'lana')
def query_photo(inline_query):
    try:
        r = types.InlineQueryResultPhoto('1',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/kitten.jpg',
                                         input_message_content=types.InputTextMessageContent('hi'))
        r2 = types.InlineQueryResultPhoto('2',
                                          'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Lana_Rhoades_cropped.jpg/820px-Lana_Rhoades_cropped.jpg',
                                          'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Lana_Rhoades_cropped.jpg/820px-Lana_Rhoades_cropped.jpg')
        bot.answer_inline_query(inline_query.id, [r, r2], cache_time=1)
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: query.query == 'video')
def query_video(inline_query):
    try:
        r = types.InlineQueryResultVideo('1',
                                         'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
                                         'video/mp4', 'Video',
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                                         'Title'
                                         )
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Now , I am developing :), I think Mahdi is writing code.', types.InputTextMessageContent('Now , I am developing :) @MahdiQiamast'))
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)


def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
