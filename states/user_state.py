from aiogram.fsm.state import State, StatesGroup


class Game(StatesGroup):
    StartGame = State()
    Game = State()
    Game1 = State()