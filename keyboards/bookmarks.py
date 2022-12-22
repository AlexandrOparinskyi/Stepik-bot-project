from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicons.lexicon_ru import LEXICON
from services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    bookmarks: InlineKeyboardMarkup = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks.add(
            InlineKeyboardButton(
                text=f'{button} - {book[button][::100]}',
                callback_data=str(button)
            )
        )
    bookmarks.add(
        InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_doolmarks'
        ),
        InlineKeyboardMarkup(
            text=LEXICON['cancel'],
            callback_data='cancel'
        )
    )
    return bookmarks


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    bookmarks: InlineKeyboardMarkup = InlineKeyboardMarkup()
    for button in sorted(args):
        bookmarks.add(
            InlineKeyboardButton(
                text=f'{LEXICON["del"]} {button} - {book[button][::100]}',
                callback_data=f'{button}del'
            )
        )
    bookmarks.add(
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        )
    )
    return bookmarks
