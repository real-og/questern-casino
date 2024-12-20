from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import aior
import logic


@dp.message_handler(commands=['begin'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_id) not in ['520251635', '6150574145']:
        return
    await logic.write_to_file(message.text)
    users = await aior.get_numbers_from_list('users')
    await logic.broadcast_red_black(users)
    await message.answer('ok')


@dp.message_handler(commands=['close'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_id) not in ['520251635', '6150574145']:
        return
    await logic.write_to_file(message.text)
    users = await aior.get_numbers_from_list('users')
    await logic.broadcast_close(users)
    await message.answer('ok')


@dp.message_handler(commands=['result'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_id) not in ['520251635', '6150574145']:
        return
    await logic.write_to_file(message.text)
    users = await aior.get_numbers_from_list('users')
    points = await logic.broadcast_result(users)

    await message.answer('ok')




        
    