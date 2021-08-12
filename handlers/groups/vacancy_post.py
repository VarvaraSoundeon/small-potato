from aiogram import types

from keyboards.inline.link_menu import const_link_menu

from data import config
from loader import dp

# if the text contains any string
@dp.message_handler(text_contains='#кандидат')
@dp.message_handler(text_contains='#работа')
@dp.message_handler(text_contains='#вакансия')
async def text_contains_vacancy_tag(message: types.Message):
    keyboard = const_link_menu('Кошелек юмани',config.UMONEY)
    keyboard.add(types.InlineKeyboardButton('BITCOIN',config.BITCOINQR))
    
    await message.reply("Привет!, чтобы запостить у лицея 239\n - сделайте перевод 100р",  reply_markup=keyboard)