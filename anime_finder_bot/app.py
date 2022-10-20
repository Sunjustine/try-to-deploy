async def on_startup(dp):
    import filters

    filters.setup(dp=dp)

    from loader import db

    from utils.db_api.db_anime_users import on_startup
    print('Відбувається підключення до Postgres...')
    await on_startup(db)

    # print('Видалення бази даних...')
    # await db.gino.drop_all()

    print('Створення таблиць...')
    await db.gino.create_all()

    print('Все готово 😎')

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp=dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp=dp)

    print("Bot set up")


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)




