from keyboards.inline.link_menu import const_link_menu
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from data import config
# from keyboards import payment

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.reply("Привет!\nХотите запостить вакансию\nв чате 39 лицея СПБ?", reply_markup=const_link_menu('линк на юмани',config.UMONEY))