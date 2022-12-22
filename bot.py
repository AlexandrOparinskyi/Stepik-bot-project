import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import load_config
from handlers.other_handlers import register_other_handlers
from handlers.user_handlers import register_user_handlers
from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)


def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_other_handlers(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Bot started')
    config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    await set_main_menu(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    except:
        await bot.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        logger.error('Bot dont started!!!')
