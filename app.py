import asyncio

from crystalpayio import CrystalPayIO
from config import LOGIN, SECRET

async def main():
    async with CrystalPayIO(LOGIN, SECRET) as crystalpayio:
        invoice_create = await crystalpayio.invoice.create(1, 10, "purchase")
        invoice_get = await crystalpayio.invoice.get(invoice_create.id)
        print(invoice_get)
        

if __name__ == "__main__":
    asyncio.run(main())