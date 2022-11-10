# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder
# from bot_commands import *


# app = ApplicationBuilder().token("5676506137:AAHs1bkWgoA6YbIklic8YT-6Lsg_LfpUPIk").build()

# app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("time", time_command))
# app.add_handler(CommandHandler("help", help_command))
# # app.add_handler(CommandHandler("sum", sum_command))
# print('start')
# app.run_polling()

#################################################################33
# updater = Updater('5676506137:AAHs1bkWgoA6YbIklic8YT-6Lsg_LfpUPIk')

# updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
# updater.dispatcher.add_handler(CommandHandler('time', time_command))
# updater.dispatcher.add_handler(CommandHandler('help', help_command))
# # updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

# print('server start')

# updater.start_polling()
# updater.idle()
##########################################################################

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# from bot_commands import *
# updater = Updater('5676506137:AAHs1bkWgoA6YbIklic8YT-6Lsg_LfpUPIk')
# updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
# updater.dispatcher.add_handler(CommandHandler('time', time_command))
# updater.dispatcher.add_handler(CommandHandler('help', help_command))
# updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
# print('server start')
# updater.start_polling()
# updater.idle()

# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

# def hi_command(update: Update, context: CallbackContext):
# #     log(update, context)
#     update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# updater = Updater('5676506137:AAHs1bkWgoA6YbIklic8YT-6Lsg_LfpUPIk')

# updater.dispatcher.add_handler(CommandHandler('hi', hi_command))

# updater.start_polling()
# updater.idle()


# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello  {update.effective_user.first_name}')


# app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()

import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "5613754283:AAEmbQPqrJCEV5lJcTq-ZksvKXEVZV94wtY"
MSG = "{}, пора делать домашнее задание!"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")

    for i in range(7):
        time.sleep(60*60*24)
        await bot.send_message(user_id, MSG.format(user_name))

if __name__ == '__main__':
    executor.start_polling(dp)