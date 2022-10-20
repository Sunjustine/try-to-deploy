from aiogram import types
from loader import dp


@dp.message_handler()
async def buttons_text(message: types.Message):
  await message.answer(f'Не розумію команди: {message.text}')