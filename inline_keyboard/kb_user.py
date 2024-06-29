from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import DB_NAME
from utils.database import Database


db = Database(DB_NAME)


def join():
    row = [InlineKeyboardButton(text="Qo'shlish", callback_data='asdfghjklmnpqrstvwxyz')]
    rows = [row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup

