from aiogram.fsm.state import StatesGroup, State


class RepoNameState(StatesGroup):
    username = State()
    repo_name = State()
