import asyncio

from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from config import DB_NAME
from inline_keyboard.kb_user import join
from states.user_state import Game
from utils.database import Database


cmd_router = Router()
db = Database(DB_NAME)


@cmd_router.callback_query(F.data == 'asdfghjklmnpqrstvwxyz')
async def cb_k(callback: CallbackQuery):
    try:
        if db.get_user_game(callback.from_user.id, callback.message.chat.title):
            await callback.bot.send_message(text="siz o'yindasiz", chat_id=callback.from_user.id)
        else:
            db.add_users_game(callback.from_user.id, callback.from_user.first_name, callback.message.chat.title)
            users = db.get_users_game(callback.message.chat.title)
            s = "Ro'yhatdan o'tish boshlandi:\n\n"
            for i in users:
                s += f"<a href='tg://user?id={i[0]}'>{i[1]}</a>, "
            await callback.message.edit_text(text=s, reply_markup=join())
    except Exception as e:
        print(e)


@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    try:
        if db.get_user(tg_id=message.from_user.id) is None:
            db.add_user(f_name=message.from_user.first_name, tg_id=message.from_user.id)
        await message.answer(
            text=f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> xush kelibsiz")
    except Exception as e:
        print(e)


@cmd_router.message(Command("game"))
async def game_handler(message: Message, state: FSMContext):
    if message.chat.title is not None:
        await state.set_state(Game.StartGame)
        res = db.create_table(message.chat.title)
        if res:
            await message.answer(text="Ro'yhatdan o'tish boshlandi:", reply_markup=join())
        else:
            await message.answer(reply_to_message_id=message.message_id, text="Ro'yhatdan o'tish boshlangan")
    else:
        await message.answer(reply_to_message_id=message.message_id, text="o'yni bureda boshlab bo'maydi")


@cmd_router.message(Command('stop'))
async def cmd_stop(message: Message):
    if message.chat.title is not None:
        db.delete_table(message.chat.title)
        await message.answer(text="o'yin to'xtatildi")
    else:
        await message.answer(reply_to_message_id=message.message_id, text="o'yni bureda to'xtatib bo'lmaydi")


@cmd_router.message(Command('test'))
async def test(message: Message):
    await message.delete()

    await message.answer(text="test")
    await asyncio.sleep(10)
    try:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)
    except:
        pass
