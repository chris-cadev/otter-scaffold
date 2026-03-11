from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_maker


async def get_greetings() -> list[dict]:
    async with async_session_maker() as session:
        result = await session.execute(
            select(Greeting).order_by(Greeting.created_at.desc())
        )
        greetings = result.scalars().all()
        return [
            {
                "id": g.id,
                "name": g.name,
                "message": g.message,
                "created_at": g.created_at.isoformat(),
            }
            for g in greetings
        ]


async def create_greeting(name: str, message: str) -> Greeting:
    async with async_session_maker() as session:
        greeting = Greeting(name=name, message=message)
        session.add(greeting)
        await session.commit()
        await session.refresh(greeting)
        return greeting
