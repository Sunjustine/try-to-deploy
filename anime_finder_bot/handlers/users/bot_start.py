from aiogram import types
from loader import dp

from filters import isPrivate
from aiogram.dispatcher.filters import CommandStart
from utils.db_api import quick_commands as commands
from aiogram.types import InputFile
from keyboards.inline.default_inline_keyboard import inline_menu


@dp.message_handler(isPrivate(), CommandStart())
async def command_start(message: types.Message):
    args = message.get_args()  # /start 13980380
    print(args)
    new_args = await commands.check_args(args, message.from_user.id)
    print(new_args)

    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            photo = InputFile("D:\\rootPython\\anime_finder_bot\\media\\pictures\\main\\hjlihjuh.jpg")

            await dp.bot.send_photo(chat_id=message.from_user.id,
                                    photo=photo,
                                    caption=f"Вітаю {message.from_user.first_name}! 👋 Ти завітав(ла) до чат-бота "
                                            f"AnimeFinderBot. " +
                                            f"Я допомжу знайти тобі цікаві аніме 🕵️‍ та зберегти їх у бібліотеку, "
                                            f"якщо буде бажання передивитися за чашкою гарячого шоколаду ☕. " +
                                            f"Зараз тут дуже обмежений каталог аніме, але ми виправимо це пізніше 🤗.",
                                    reply_markup=inline_menu)
        elif user.status == 'baned':
            await message.answer('Ви забанені, поводьте себе краще')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                second_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active',
                                phone_number=0)
        # try:
        #     await dp.bot.send_message(chat_id=int(new_args),
        #                               text=f'По товєму посиланню зареєструвався {message.from_user.first_name}')
        # except Exception:
        #     pass


@dp.message_handler(isPrivate(), text='/ban')
async def get_ban(message: types.message):
    await commands.update_status(user_id=message.from_user.id, status='baned')
    await message.answer('Ви заблоковані')


@dp.message_handler(isPrivate(), text='/unban')
async def get_unban(message: types.message):
    await commands.update_status(user_id=message.from_user.id, status='active')
    await message.answer('Вітаю, ви розблоковані')


@dp.message_handler(isPrivate(), text='/profile')
async def profile(message: types.message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'Інформація про юзера:\n'
                         f'user_id - {user.user_id},\n'
                         f'first_name - {user.first_name},\n'
                         f'second_name - {user.second_name},\n'
                         f'username - {user.username},\n'
                         f'status - {user.status}')
