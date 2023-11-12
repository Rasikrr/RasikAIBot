import asyncio
import os
import sys

sys.path.append("../keyboards.py")
sys.path.append("../create_bot.py")
from keyboards import get_main_kb, get_developer_socials, get_return_button
from create_bot import dp, bot, bard
from dotenv import load_dotenv
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext, storage
from datetime import datetime


load_dotenv()
# States


class AI(StatesGroup):
    inf = State()


class Report(StatesGroup):
    report_text = State()


# Start command
async def command_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}", reply_markup=get_main_kb())


async def get_my_socials(message: types.Message):
    await message.answer("Telegram: @Rasikrr\n Instagram: https.rasikrr")


# Finish states
async def finish_states(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("How can I help You? 😊", reply_markup=get_main_kb())


async def back_to_menu(message: types.Message):
    await message.answer("How can I help You? 😊", reply_markup=get_main_kb())


# Ask from AI
async def ai(message: types.Message):
    await message.answer("Ask something from AI: ", reply_markup=get_return_button())
    await AI.inf.set()


async def ask_from_ai(message: types.Message, state: FSMContext):
    if message.text in ("Return to menu", "/start"):
        await finish_states(message, state)
    else:
        try:
            await message.answer("typing...")
            async with state.proxy() as data:
                data["inf"] = message.text
            await message.answer(bard.answer(data["inf"]))
        except:
            await message.answer("Sorry, something went wrong. Write your answer again")
        await AI.inf.set()


# Report about the problem
async def report_about_problem(message: types.Message):
    await message.answer("Talk about your problem: ", reply_markup=get_return_button())
    await Report.report_text.set()


async def get_report_text(message: types.Message, state: FSMContext):
    if message.text in ("Return to menu", "/start"):
        await finish_states(message, state)
    else:
        async with state.proxy() as data:
            data["report"] = message.text
        user_message = f"{message.from_user.first_name} {message.from_user.last_name}\n{str(datetime.now()).split('.')[0]}:\n{data['report']}"
        await bot.send_message(os.getenv("GROUP_REPORT_ID"), user_message)
        await message.answer("Thank you for your report! I'll be sure to fix it. 😁", reply_markup=get_developer_socials())
        await state.finish()


def registration_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(get_my_socials, text="Get developers socials 📱")
    dp.register_message_handler(ai, text="Ask the AI 🧠")
    dp.register_message_handler(ask_from_ai, state=AI.inf)
    dp.register_message_handler(report_about_problem, text="Report the problem ⛔")
    dp.register_message_handler(get_report_text, state=Report.report_text)
    dp.register_message_handler(back_to_menu, text="Return to menu")

