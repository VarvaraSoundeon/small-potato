from aiogram import types

from keyboards.inline.link_menu import const_link_menu

from data import config
from loader import dp

# if the text contains any string
@dp.message_handler(text_contains='#кандидат')
@dp.message_handler(text_contains='#работа')
@dp.message_handler(text_contains='#вакансия')
async def text_contains_vacancy_tag(message: types.Message):
    await message.reply("Привет!, {message.from_user.full_name}!\nХотите запостить вакансию\nв чате 39 лицея СПБ?", reply_markup=const_link_menu('линк на юмани',config.UMONEY))