from aiogram.types import CallbackQuery
from loader import dp
import re


from keyboards.inline_commands.search_commands import *
from aiogram.utils.markdown import hlink


@dp.callback_query_handler(text='news')
async def send_message(call: CallbackQuery):
    dict_of_news = await get_news()
    for i in range(0, len(dict_of_news['img'])):
        string = "".join(dict_of_news["desc"][i])
        pattern = '[+|.]'
        await call.message.answer_photo(photo=dict_of_news['img'][i],
                                        caption=f'{re.sub(pattern, "", string)} + {hlink("Дізнатися більше", dict_of_news["link"][i])}')