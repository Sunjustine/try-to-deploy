from aiogram.types import CallbackQuery
from loader import dp
from filters import isPrivate


@dp.callback_query_handler(isPrivate(), text='library')
async def send_message(call: CallbackQuery):
    await call.message.answer('Ти вибрав бібліотеку')
