from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', "Увійти у головне меню бота"),
        types.BotCommand('help', "Допомога при користуванні ботом"),
        types.BotCommand('profile', "Профіль користувача"),
        types.BotCommand('register', "Реєстрація нового користувача")
    ])
