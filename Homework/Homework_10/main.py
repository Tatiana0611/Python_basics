# from telegram import Update
# from bot_commands import *
import requests
import logging
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

# https://demo.deeppavlov.ai/#/ru/ner

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = 'https://7015.deeppavlov.ai/model'

CHOICE, RATIONAL_ONE, RATIONAL, RATIONAL_TWO, OPERATIONS_RATIONAL, OPERATIONS_COMPLEX, COMPLEX_ONE, COMPLEX_TWO = range(8)

def start(update, _):
    reply_keyboard = [['Операции с рациональными числами','Настроение', 'Операции с комплесными числами', 'Cancel']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Добро пожаловать в калькулятор.', reply_markup=markup_key)
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    logger.info('Выбор операции: %s: %s', user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice == 'Операции с рациональными числами':
        update.message.reply_text('Введите первое рациональное число')
        return RATIONAL_ONE
    if user_choice == 'Настроение':
        update.message.reply_text('Введите фразу')
        return RATIONAL
    if user_choice == 'Cancel':
        return cancel(update, context)

def rational(update, context):
    data = {'x': [update.message.text]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    print(res[0][0])
    print(res)
    update.message.reply_text(res[0][0])
    return start(update, context)

def rational_one(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввел число %s: %s', user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_one'] = get_rational
        update.message.reply_text('Введите второе рациональное число')
        return RATIONAL_TWO
    


def rational_two(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввел число %s: %s', user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_two'] = get_rational
        reply_keyboard = [['+', '-', '*', '/']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Выберите операцию с числами', reply_markup=markup_key)
        return OPERATIONS_RATIONAL


def operations_rational(update, context):
    user = update.message.from_user
    logger.info('Пользователь выбрал операцию %s: %s', user.first_name, update.message.text)
    rational_one = context.user_data.get('rational_one')
    rational_two = context.user_data.get('rational_two')
    user_choice = update.message.text
    if user_choice == '+':
        result = rational_one + rational_two
    if user_choice == '-':
        result = rational_one - rational_two
    if user_choice == '*':
        result = rational_one * rational_two
    if user_choice == '/':
        result = rational_one / rational_two
    update.message.reply_text(f'Результат выбранной операции: {result}')
    return start(update, context)

def cancel(update, _):
    user = update.message.from_user
    logger.info('Пользователь отменил разговор.', user.first_name)
    update.message.reply_text('Отмена')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            RATIONAL: [MessageHandler(Filters.text, rational)],
            RATIONAL_ONE: [MessageHandler(Filters.text, rational_one)],
            RATIONAL_TWO: [MessageHandler(Filters.text, rational_two)],
            OPERATIONS_RATIONAL: [MessageHandler(Filters.text, operations_rational)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conversation_handler)

updater.start_polling()
updater.idle()


# updater = Updater('5613754283:AAEmbQPqrJCEV5lJcTq-ZksvKXEVZV94wtY')

# updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
# updater.dispatcher.add_handler(CommandHandler('time', time_command))
# updater.dispatcher.add_handler(CommandHandler('help', help_command))
# updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

# print('server start')
# updater.start_polling()
# updater.idle()
