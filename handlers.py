from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message

import kb
import text

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

@router.message(F.text == "Меню")
# @router.message(F.text == "Выйти в меню")
# @router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer('..вызов меню..')

@router.message()
async def message_handler(msg: Message):
    if msg.text.lower() == 'маняша':
        await msg.answer("МА-НЯ-ША !")
    else:
        await msg.answer(f"Твой ID: {msg.from_user.id}")