import asyncio
import redis.asyncio as redis
import asyncio
import json

async def add_number_to_list(redis_key, number):
    nums = await get_numbers_from_list(redis_key)
    if int(number) in nums:
        return 

    # Создаем одно соединение с Redis
    client = redis.Redis(host='localhost', port=6379, db=3)
    
    # Добавляем число в список
    await client.rpush(redis_key, number)

    # Закрываем соединение с Redis
    await client.close()




async def get_numbers_from_list(redis_key):
    # Создаем одно соединение с Redis
    client = redis.Redis(host='localhost', port=6379, db=3)
    
    # Извлекаем числа из списка

    numbers = await client.lrange(redis_key, 0, -1)
    await client.close()

    return [int(num) for num in numbers]


async def set_json(redis_key, data):
    """Сохранение Python-словаря в Redis как JSON"""
    # Создаем асинхронное соединение с Redis
    client = redis.Redis(host='localhost', port=6379, db=3)

    # Сериализуем Python-словарь в строку JSON
    json_data = json.dumps(data)

    # Сохраняем строку JSON в Redis
    await client.set(redis_key, json_data)

    # Закрываем соединение
    await client.close()
    print(f"JSON сохранен в Redis по ключу {redis_key}")

async def get_json(redis_key):
    """Получение JSON из Redis и десериализация в Python-словарь"""
    # Создаем асинхронное соединение с Redis
    client = redis.Redis(host='localhost', port=6379, db=3)

    # Получаем строку JSON из Redis
    json_data = await client.get(redis_key)

    # Если данные найдены
    if json_data:
        # Десериализуем строку JSON обратно в Python-словарь
        data = json.loads(json_data)
        await client.close()
        return data
    else:
        await client.close()
        print(f"Данные с ключом {redis_key} не найдены.")
        return None