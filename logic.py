import asyncio
import aiofiles
from loader import bot
import keyboards as kb
import aior


async def get_result(id, round):
    data = await aior.get_json(str(id))
    points = 0
    text = '-'
    if round == '1': 
        if data.get('col1') == 'red':
            points = 10
        if data.get('val1') == '23':
            points = 30
        if data.get('val1') == '23' and data.get('col1') == 'red':
            points = 50
        text = f"""ИТОГИ РАУНДА 1: 🔴 / 2️⃣3️⃣ \nВ этом раунде вы выиграли {points} баллов. Поздравляем! 🎉 """
    elif round == '2':
        if data.get('col2') == 'red':
            points = 10
        if data.get('val2') == '1':
            points = 30
        if data.get('val2') == '1' and data.get('col2') == 'red':
            points = 50
        text = f"""ИТОГИ РАУНДА 2: 🔴 / 1️⃣ \nВ этом раунде вы выиграли {points} баллов. Поздравляем! 🎉 """
    elif round == '3':
        if data.get('col3') == 'black':
            points = 10
        if data.get('val3') == '4':
            points = 30
        if data.get('val3') == '4' and data.get('col3') == 'black':
            points = 50
        text = f"""ИТОГИ РАУНДА 3: ⚫️ / 4️⃣ \nВ этом раунде вы выиграли {points} баллов. Поздравляем! 🎉 """
    elif round == '4':
        if data.get('col4') == 'black':
            points = 10
        if data.get('val4') == '29':
            points = 30
        if data.get('val4') == '29' and data.get('col4') == 'black':
            points = 50
        text = f"""ИТОГИ РАУНДА 4: ⚫️ / 2️⃣9️⃣\nВ этом раунде вы выиграли {points} баллов. Поздравляем! 🎉 """
    elif round == '5':
        if data.get('col5') == 'red':
            points = 10
        if data.get('val5') == '34':
            points = 30
        if data.get('val5') == '34' and data.get('col5') == 'red':
            points = 50
        text = f"""ИТОГИ РАУНДА 5: 🔴 / 3️⃣4️⃣ \nВ этом раунде вы выиграли {points} баллов. Поздравляем! 🎉 """
    return text, points


async def write_to_file(data):
    async with aiofiles.open('state.txt', 'w') as file:
        await file.write(data) 
        


async def read_from_file():
    async with aiofiles.open('state.txt', 'r') as file:
        content = await file.read()  
        return content
    

async def broadcast_red_black(user_ids):
    for user_id in user_ids:
        await bot.send_message(user_id, 'Выбирайте цвет', reply_markup=kb.red_black_kb)


async def broadcast_close(user_ids):
    for user_id in user_ids:
        await bot.send_message(user_id, 'Прием ставок закрыт')

async def broadcast_result(user_ids):
    round = await read_from_file()
    round = round.strip().split()[1]

    for user_id in user_ids:
        text, points = await get_result(str(user_id), round)
        await bot.send_message(user_id, text)
    return points
        
