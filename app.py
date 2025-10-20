import asyncio

from crystalpayio import CrystalPayIO
from config import LOGIN, SECRET

async def main():
    async with CrystalPayIO(LOGIN, SECRET) as crystalpayio:
        await crystalpayio.checkout.balance()
        

if __name__ == "__main__":
    asyncio.run(main())