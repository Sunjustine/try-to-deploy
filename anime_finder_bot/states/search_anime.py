from aiogram.dispatcher.filters.state import StatesGroup, State


class Search(StatesGroup):
    name = State()
    choose_anime = State()
    player = State()
    series = State()
    video = State()
