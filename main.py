import os

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from chat_gpt import gpt

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
openai_api_key = os.getenv('openai_api_key')

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Привет, я бот ChatGPT!\n"
                         "Чем я могу тебе помочь?")


@dp.message()
async def message(message: types.Message):
    await message.answer("Ожидайте ответ...")
    await message.reply(gpt(message.text))
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)


if __name__ == '__main__':
    dp.run_polling(bot)
