import asyncio

from crystalpayio import CrystalPayIO
from config import LOGIN, SECRET

async def main():
    async with CrystalPayIO(LOGIN, SECRET) as crystalpayio:
        x = await crystalpayio.payment.edit(method="TEST", extra_commission_percent=0, enabled=True)
        print(x)
        

if __name__ == "__main__":
    asyncio.run(main())