from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

find_buttons = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Перегляд', callback_data='watch_video'),
                                            InlineKeyboardButton(text='Коменти', callback_data='comments')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Більше', callback_data='more_info')
                                        ]
                                    ])
