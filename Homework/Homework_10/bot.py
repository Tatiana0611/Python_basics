import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

CHOICE, NUMBER_ONE, NUMBER_TWO, OPERATIONS = range(4)

def start(update, _):
    reply_keyboard = [['Калькулятор', 'Отмена']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Выберите действие', reply_markup=markup_key)
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    logger.info('Операция: %s: %s', user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice == 'Калькулятор':
        update.message.reply_text('Введите первое число')
        return NUMBER_ONE
    if user_choice == 'Отмена':
        return cancel(update, context)

def number_one(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввел число %s: %s', user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_one'] = get_number
        update.message.reply_text('Введите второе число')
        return NUMBER_TWO

def number_two(update, context):
    user = update.message.from_user
    logger.info('Пользователь ввел число %s: %s', user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_two'] = get_number
        reply_keyboard = [['+', '-', '*', '/']]
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text('Выберите операцию с числами', reply_markup=markup_key)
        return OPERATIONS

def operations(update, context):
    user = update.message.from_user
    logger.info('Пользователь выбрал операцию %s: %s', user.first_name, update.message.text)
    number_one = context.user_data.get('number_one')
    number_two = context.user_data.get('number_two')
    user_choice = update.message.text
    if user_choice == '+':
        result = number_one + number_two
    if user_choice == '-':
        result = number_one - number_two
    if user_choice == '*':
        result = number_one * number_two
    if user_choice == '/':
        result = number_one / number_two
    update.message.reply_text(f'Результат выбранной операции: {result}')
    return start(update, context)

def cancel(update, _):
    user = update.message.from_user
    logger.info('Пользователь отменил разговор.', user.first_name)
    update.message.reply_text('Работа с калькулятором завершена')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            NUMBER_ONE: [MessageHandler(Filters.text, number_one)],
            NUMBER_TWO: [MessageHandler(Filters.text, number_two)],
            OPERATIONS: [MessageHandler(Filters.text, operations)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conversation_handler)

updater.start_polling()
updater.idle()