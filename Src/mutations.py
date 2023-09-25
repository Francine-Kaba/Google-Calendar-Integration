from prisma import Prisma
from graphql import GraphQLError
from helpers.prisma_connect import connect_to_prisma
from datetime import datetime

prisma = Prisma()


class Calender:

    async def try_calender(self, info, input):
        if await connect_to_prisma(prisma):
            task_name = input.get('task_name')
            email = input.get('email')

            return await prisma.calender.create(
                data={
                    'task_name': task_name,
                    'email': email,
                    'created_at': datetime.now()
                }
            )
