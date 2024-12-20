from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import aior


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.greeting)
    await message.answer(texts.ask_name)
    await State.entering_name.set()
    await aior.add_number_to_list('users', int(message.from_user.id))
    await aior.set_json(str(message.from_id), {'name': None,
                                               'col1': None,
                                               'val1': None,
                                               'col2': None,
                                               'val2': None,
                                               'col3': None,
                                               'val3': None,
                                               'col4': None,
                                               'val4': None,
                                               'col5': None,
                                               'val5': None,
                                               'res1': None,
                                               'res2': None,
                                               'res3': None,
                                               'res4': None,
                                               'res5': None,})
                                            

    