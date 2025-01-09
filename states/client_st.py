from aiogram.fsm.state import State, StatesGroup

class start_state(StatesGroup):
    choose = State()
    train = State()
    tip = State()
    cur = State()
    prev = State()
    post_start = State()
    post_number = State()
    list_of_phrases = State()
    theme_number = State()
    start = State()
    Da = State()
    proverka = State()