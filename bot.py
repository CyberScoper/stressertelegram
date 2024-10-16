from telethon import TelegramClient
import asyncio
import random
import string

# Ваш api_id и api_hash
api_id = ####
api_hash = '####'

# Ваш телефонный номер
phone_number = '####'

# Создаем клиента
client = TelegramClient('stress_test', api_id, api_hash)

# Функция для генерации строки из случайных символов
def generate_broken_string(length=1000):
    chars = string.ascii_letters + string.digits + string.punctuation + " \n\t"
    return ''.join(random.choice(chars) for _ in range(length))

# Асинхронная функция для отправки сообщений
async def send_message_to_bot(bot_username, num_requests):
    async with client:
        for i in range(num_requests):
            # Генерация "ломаного" сообщения из 1000 случайных символов
            broken_message = generate_broken_string()

            # Отправляем сообщение с "ломаными" символами
            await client.send_message(bot_username, broken_message)
            print(f'Запрос {i+1}: Отправлено ломаное сообщение боту {bot_username}')

            # Задержка между запросами
            await asyncio.sleep(1)

# Основная функция для запуска
def stress_test(bot_username, num_requests):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_message_to_bot(bot_username, num_requests))

if __name__ == '__main__':
    client.start(phone=phone_number)  # Логинимся в Telegram

    # Вводим username бота для атаки
    bot_username = input("Введите username бота (например, @bot): ")

    # Вводим количество запросов
    num_requests = int(input("Введите количество запросов: "))
    
    # Запускаем стресс-тест
    stress_test(bot_username, num_requests)
