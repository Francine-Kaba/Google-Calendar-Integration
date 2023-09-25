from prisma import Prisma
from helpers.prisma_connect import connect_to_prisma

prisma = Prisma()


class CalenderQuery:
    # Listing all users
    async def list_calender(self, info):
        if await connect_to_prisma(prisma):
            return await prisma.calender.find_many(
                order={
                    'id': 'desc'
                }
            )
