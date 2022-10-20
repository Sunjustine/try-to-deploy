from utils.db_api.schemas.anime_user import User
from asyncpg import UniqueViolationError
from utils.db_api.db_anime_users import db


async def add_user(user_id: int, first_name: str, second_name: str, username: str, status: str, phone_number: int):
    try:
        user = User(user_id=user_id, first_name=first_name, second_name=second_name, username=username,
                    status=status, phone_number=phone_number)
        await user.create()
    except UniqueViolationError:
        print('user doesn\'t append')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_of_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_status(user_id, status):
    user = await select_user(user_id=user_id)
    await user.update(status=status).apply()


async def update_phone(user_id, phone_number):
    user = await select_user(user_id=user_id)
    await user.update(phone_number=phone_number).apply()


async def check_args(args, user_id: int):
    if args == '':
        args = '0'
        return args

    elif not args.isnumeric():
        args = '0'
        return args

    elif args.isnumeric():
        if int(args) == user_id:
            return args

        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args

        else:
            args = str(args)
            return args

    else:
        args = '0'
        return args


# async def count_of_refs(user_id):
#     refs = await User.query.where(User.referral_id == user_id).gino.all()
#     return len(refs)
