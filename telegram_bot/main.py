from aiogram import executor
from create_bot import dp
from handlers import client


async def start(_):
    print("The Bot is successfully running")


client.registration_handler_client(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=start)