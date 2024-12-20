from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts

start_kb = ReplyKeyboardMarkup([[texts.start_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

red_black_kb = InlineKeyboardMarkup(row_width=2)
button_black = InlineKeyboardButton("ЧЁРНОЕ", callback_data="black")
button_red = InlineKeyboardButton("КРАСНОЕ", callback_data="red")
red_black_kb.add(button_black, button_red)



numbers_kb = InlineKeyboardMarkup(row_width=4) 
for i in range(1, 37):
    button = InlineKeyboardButton(str(i), callback_data=str(i))
    numbers_kb.insert(button) 
    # numbers_kb.add(button) 
    

