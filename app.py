import asyncio

from crystalpayio import CrystalPayIO
from config import LOGIN, SECRET

async def main():
    async with CrystalPayIO(LOGIN, SECRET) as crystalpayio:
        x = await crystalpayio.invoice.create(1, 10, "purchase")
        print(x)
        

if __name__ == "__main__":
    asyncio.run(main())