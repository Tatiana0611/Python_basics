from telegram import Update
from bot_commands import *
import requests
# import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext
)
# from spy import *

CHOICE, RATIONAL_ONE, RATIONAL, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(8)

def start(update, _):
    reply_keyboard = [['Операции с рациональными числами','Настроение', 'Операции с комплесными числами', 'Cancel']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в калькулятор.', reply_markup=markup_key)
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    # logger.info('Выбор операции: %s: %s', user.first_name, update.message.text)
    user_choice = update.message.text
    if user.choice == 'Операции с рациональными числами':
        update.message.reply_text('Введите первое рациональное число')
        return RATIONAL_ONE


# def hi_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# def help_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'/hi\n/time\n/help')

# def time_command(update: Update, context: CallbackContext):
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')

# def sum_command(update: Update, context: CallbackContext):
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split() # /sum 34 65
#     x = int(items[1])
#     y = int(items[2])
#     update.message.reply_text(f'{x} + {y} = {x+y}')