"""
 2This is a echo bot.
 3It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
import wikipedia
wikipedia.set_lang('uz')
API_TOKEN = '1916907969:AAHaQ7JQnYm8wrr-fgvEGjKHw6OW0n1UHbc'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
23    This handler will be called when user sends `/start` or `/help` command
24    """
    await message.reply("Salom Startni bosgan odam men endi seni buyrug'ingni bajaradigan botman.")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu so\'z haqida ma\'lumot topilmadi kechirasiz.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
