from aiogram.fsm.state import State, StatesGroup

class start_state(StatesGroup):
    chooseStandart = State()
    chooseDa = State()
    train = State()
    tip = State()
    cur = State()
    prev = State()
    list_of_phrases = State()
    theme_number = State()
    start = State()
    Da = State()