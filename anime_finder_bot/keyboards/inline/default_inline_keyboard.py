from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_menu = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardButton(text='Новини', callback_data='news'),
                                           InlineKeyboardButton(text='Бібліотека', callback_data='library')
                                       ],
                                       [
                                           InlineKeyboardButton(text='Пошук', callback_data='search'),
                                           InlineKeyboardButton(text='Реєстрація', callback_data='register')

                                       ]
                                   ])
