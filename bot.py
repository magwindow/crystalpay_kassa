import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import BOT_TOKEN, LOGIN, SECRET

from crystalpayio import CrystalPayIO

router = Router()
crystalpayio = CrystalPayIO(LOGIN, SECRET)


async def state(id, message):
    while True:
        info = await crystalpayio.invoice.get(id)
        print("Created: ", info.state)
        if info.state == "payed":
            await message.answer("Оплачено")
            print("Paid: ", info.state)
            break
        else:
            await message.answer("Не Оплачено")
            print("Not paid: ", info.state)
        await asyncio.sleep(30)


@router.message(CommandStart())
async def start(message: Message):
    invoice = await crystalpayio.invoice.create(amount=1, lifetime=10, type="purchase", amount_currency="USD")
    await message.answer(invoice.url)
    
    asyncio.create_task(state(invoice.id, message))


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())