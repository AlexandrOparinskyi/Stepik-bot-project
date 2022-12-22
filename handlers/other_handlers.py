from aiogram import Dispatcher
from aiogram.types import Message


async def send_echo(message: Message):
    await message.answer(f'Это {message.text}')


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(send_echo)
