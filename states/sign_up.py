from aiogram.dispatcher.filters.state import State, StatesGroup

class sign(StatesGroup):
    name = State()
    age = State()
    phone = State()
    email = State()
