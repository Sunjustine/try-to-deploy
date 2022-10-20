from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from requests_html import AsyncHTMLSession

from keyboards.inline_commands.search_commands import *
from loader import dp
from states import Search


@dp.callback_query_handler(text='search')
async def send_message(call: types.CallbackQuery):
    await call.message.answer(f'Введи назву аніме, наприклад: \"Сайтама\" 🦸')
    await Search.name.set()


''' Func handler name of anime. Return collection of anime cards '''


@dp.message_handler(state=Search.name)
async def state1(message: types.Message, state: FSMContext):
    # name_anime = call.message.text

    name_anime = message.text
    await state.update_data(name=name_anime)

    data = await state.get_data()

    videocards = await get_video_from_site(data.get('name'))

    dict_video_id = {}

    if not videocards['link']:
        await message.answer(f'Аніме \"{str(data.get("name"))}\" немає в списку, спробуй інше 😉')
    else:
        for i in range(0, len(videocards['img'])):
            link_id = videocards["link"][i].split("/")[3].split("-")[0]

            await message.answer_photo(photo=videocards['img'][i],
                                       caption=f'<b>{videocards["name"][i]}</b>'
                                               f'\n\n'
                                               f'{"".join(videocards["desc"][i][0:170])}....',
                                       reply_markup=InlineKeyboardMarkup(row_width=2,
                                                                         inline_keyboard=[
                                                                             [
                                                                                 InlineKeyboardButton(
                                                                                     text='Перегляд',
                                                                                     callback_data=f'{link_id}-watch'),
                                                                                 InlineKeyboardButton(
                                                                                     text='Коменти',
                                                                                     callback_data=f'{link_id}-comm')
                                                                             ],
                                                                             [
                                                                                 InlineKeyboardButton(
                                                                                     text='Більше',
                                                                                     callback_data=f'{link_id}-more')
                                                                             ]
                                                                         ]))

            dict_video_id[f'{link_id}-watch'] = videocards['link'][i]

            await Search.choose_anime.set()

        @dp.callback_query_handler(state=Search.choose_anime, text_contains='watch')
        async def state2(call: types.CallbackQuery):

            await state.update_data(choose_anime=dict_video_id.get(f'{call.data}'))

            await call.message.answer('Пошук плеєрів, зачекай будь-ласка.... 🎙')

            link = str((await state.get_data()).get('choose_anime'))

            players = await get_anime_players(session=AsyncHTMLSession(), url=str(link))

            players_markup = InlineKeyboardMarkup()

            for index, item in enumerate(players):
                players_markup.add(InlineKeyboardButton(text=item, callback_data=f'player-{index}'))

            await call.message.answer(text="Вибери свій плеєр 👓", reply_markup=players_markup)

            await Search.player.set()

        @dp.callback_query_handler(state=Search.player, text_contains='player')
        async def state3(call: types.CallbackQuery):
            await call.message.answer('Пошук серій..... 🎞')

            await state.update_data(player=f'{call.data}'.split('-')[1])

            player_number = (await state.get_data()).get('player')

            script = """
                    () => {
                        var elements = document.getElementsByClassName("RlItem1");
                        elements[%s].click();
                    }
                """ % player_number
            link = str((await state.get_data()).get('choose_anime'))

            series = await get_anime_series(AsyncHTMLSession(), link, script)

            series_markup = InlineKeyboardMarkup()

            [series_markup.add(InlineKeyboardButton(text=serie, callback_data=f'serie-{index}')) for index, serie in
             enumerate(series)]

            await call.message.answer('Вибери серію для перегляду 🎞', reply_markup=series_markup)

            await state.finish()

        # @dp.callback_query_handler(Search.series, text_contains='serie')
        # async def state4(call: types.CallbackQuery, state: FSMContext):
        #     await call.answer('Обробка запиту по серії')
