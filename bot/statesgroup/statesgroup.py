from aiogram.dispatcher.filters.state import StatesGroup, State


class RepoNameStates(StatesGroup):
    login = State()
    reponame = State()
