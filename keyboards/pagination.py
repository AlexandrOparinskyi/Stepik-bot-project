from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicons.lexicon_ru import LEXICON


def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    pagination: InlineKeyboardMarkup = InlineKeyboardMarkup()
    pagination.row(*[InlineKeyboardButton(LEXICON[button] if button in LEXICON else button, callback_data=button) for button in buttons])
    return pagination
