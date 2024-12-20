from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import aior
import tables
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
    if message.text == '/result 5':
        await logic.broadcast_final(users)

    await message.answer('ok')


@dp.message_handler(commands=['generate'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_id) not in ['520251635', '6150574145']:
        return
    data_to_write = [['id', 'имя', 'РАУНД 1', 'РАУНД 2', 'РАУНД 3','РАУНД 4','РАУНД 5','очки']]
    users = await aior.get_numbers_from_list('users')
    for id in users:
        data = await aior.get_json(str(id))
        score = await logic.get_all_score(id)
        row = [str(id),
               data.get('name'),
               str(data.get('col1')) + str(data.get('val1')),
               str(data.get('col2')) + str(data.get('val2')),
               str(data.get('col3')) + str(data.get('val3')),
               str(data.get('col4')) + str(data.get('val4')),
               str(data.get('col5')) + str(data.get('val5')),
               str(score)
            ]
        data_to_write.append(row)
    print(data_to_write)
    tables.sheet.update_range(data_to_write, 'A1:H3000')
    await message.answer('ok')






        
    