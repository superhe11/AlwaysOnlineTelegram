import time
from telethon.sync import TelegramClient

# Функция для чтения конфигурационного файла
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

# Чтение конфигурации
config = read_config('config.txt')

# Извлечение параметров из конфигурации
api_id = int(config['api_id'])
api_hash = config['api_hash']
phone = config['phone']
update_interval = int(config['update_interval'])

# Создаём клиента
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Авторизация
    await client.start(phone)
    
    # Бесконечный цикл для поддержания активности
    while True:
        # Отправка сообщения самому себе
        message = await client.send_message('me', 'Я все еще онлайн!')
        # Удаление сообщения сразу после отправки
        await client.delete_messages('me', message.id)
        # Ожидание update_interval секунд перед следующей итерацией
        time.sleep(update_interval)

# Запуск клиента
with client:
    client.loop.run_until_complete(main())
