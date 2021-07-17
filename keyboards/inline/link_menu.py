from aiogram import Bot, Dispatcher, executor, types

from loader import dp

def const_link_menu(url_text,url_link):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness
    keyboard_markup.add(
        # url buttons have no callback data
        types.InlineKeyboardButton(url_text, url=url_link),
    )
    
    #callback-button
    """
    text_and_data = (
        ('Нет, спасибо!', 'No'),
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.row(*row_btns)
    """
    return keyboard_markup