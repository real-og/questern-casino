from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aior
import logic


@dp.message_handler(state=State.entering_name)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await aior.get_json(str(message.from_id))
    data['name'] = message.text
    await aior.set_json(str(message.from_id), data)
    await message.answer(texts.rules)
    await message.answer(texts.wrong_start_pressed, reply_markup=kb.start_kb)
    await State.after_name.set()


@dp.message_handler(state=State.after_name)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.start_btn:
        await message.answer(texts.instruction)
    else:
        await message.answer(texts.wrong_start_pressed, reply_markup=kb.start_kb)
        return
    await State.waiting.set()


@dp.callback_query_handler(state='*')
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    state = await logic.read_from_file()
    if ('close' in state) or ('result' in state):
        await callback.message.answer('Прием ставок уже завершен. Ждите следующий раунд')
        return
    data = await aior.get_json(str(callback.from_user.id))
    info = callback.data
    if info == 'black':
        if '1' in state:
            data['col1'] = 'black'
        elif '2' in state:
            data['col2'] = 'black'
        elif '3' in state:
            data['col3'] = 'black'
        elif '4' in state:
            data['col4'] = 'black'
        elif '5' in state:
            data['col5'] = 'black'
        await callback.message.edit_text('СТАВКА НА ЧИСЛО', reply_markup=kb.numbers_kb)
    elif info == 'red':
        if '1' in state:
            data['col1'] = 'red'
        elif '2' in state:
            data['col2'] = 'red'
        elif '3' in state:
            data['col3'] = 'red'
        elif '4' in state:
            data['col4'] = 'red'
        elif '5' in state:
            data['col5'] = 'red'
        await callback.message.edit_text('СТАВКА НА ЧИСЛО', reply_markup=kb.numbers_kb)
    else:
        if '1' in state:
            data['val1'] = info
        elif '2' in state:
            data['val2'] = info
        elif '3' in state:
            data['val3'] = info
        elif '4' in state:
            data['val4'] = info
        elif '5' in state:
            data['val5'] = info
        await callback.message.edit_text('☑️ Ваша ставка принята')
    print(data)
    await aior.set_json(str(callback.from_user.id), data)
    await bot.answer_callback_query(callback.id)