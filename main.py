import asyncio
import sqlite3 
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.filters.command import Command

bot = Bot(token="7760313088:AAGFLFWSTk8zjWBBxWtlTxkGT5qTxOdUW0g")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    time_on = datetime.now().strftime("%H:%M")
    await message.answer(f"""
Привет! Мой функционал:
· Я считаю сколько дней до нового года(скоро)
· Мутить (скоро)
· Приветствую новых участников (скоро, может быть)
· Умею играть в слова (скоро, может быть)
· И все остальное(может быть)
""")
    await message.answer("У меня что... Дядя на стене? 😨")

@dp.message(Command("time"))
async def say_tm(message: types.Message):
    time_on = datetime.now().strftime("%H:%M:%S, %d.%m.%Y")
    await message.reply(time_on)

@dp.message()
async def on_message(message: types.Message):
    text = message.text.lower()
    today = datetime.today().date()
    last_msg_date = ""
    with sqlite3.connect("data.db") as db:
        cur = db.cursor()
        for date in cur.execute("SELECT date FROM last_msg"):
            date = date[0]
            last_msg_date = date
    today = str(today)
    last_msg_date = str(last_msg_date)
    if today != last_msg_date:
        print("IF is continued")
        now = datetime.today()
        new_year = datetime(2025,1,1)
        data = new_year - now
        days = data.days
        minutes, seconds = divmod(data.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        await message.reply("Поздравляю, ты первый за сегодня! Кстати, до нового года {} дней, {} часов, {} минут.".format(days, hours, minutes))
        with sqlite3.connect("data.db") as db:
            db.cursor().execute("UPDATE last_msg SET date = ?", (today, ))
    if text in ["когда нг?","сколько дней до нового года?","скок до нг?","скок дней до нг?","скок до нового года?","скоро нг?"]:
        now = datetime.today()
        new_year = datetime(2025,1,1)
        data = new_year - now
        days = data.days
        minutes, seconds = divmod(data.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        await message.reply("До нового года {} дней, {} часов, {} минут".format(days, hours, minutes))

async def ini():
    print("Bot started.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(ini())