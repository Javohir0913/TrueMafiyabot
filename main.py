import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config import BOT_TOKEN
from handlers.cmd_handlers import cmd_router


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await bot.set_my_commands(
        commands=[BotCommand(command='start', description='boshlash'),
                  BotCommand(command='game', description="o'yin boshlash"),
                  BotCommand(command='stop', description="o'yini to'xtatish"),
        ]
    )
    dp = Dispatcher()
    dp.include_router(cmd_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
