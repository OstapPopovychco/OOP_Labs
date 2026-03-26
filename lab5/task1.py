import asyncio
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

DATABASE_URL = "sqlite+aiosqlite:///network_nodes.db"
Base = declarative_base()

class Node(Base):
    __tablename__ = 'nodes'
    id = Column(Integer, primary_key=True)
    ip_address = Column(String, unique=True, nullable=False)
    status = Column(String, default="unknown")

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("--- Таблиці створено ---")

async def reset_nodes():
    async with AsyncSessionLocal() as session:
        await session.execute(text("DELETE FROM nodes"))
        await session.commit()
    print("--- Базу очищено ---")

async def add_initial_nodes():
    async with AsyncSessionLocal() as session:
        nodes = [
            Node(ip_address=f"192.168.1.{i}", status="unknown")
            for i in range(1, 16)
        ]
        session.add_all(nodes)
        await session.commit()
    print(f"--- Додано {len(nodes)} вузлів ---")

async def display_nodes(label=""):
    print(f"\nСтатус вузлів ({label}):")
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Node))
        nodes = result.scalars().all()
        for node in nodes:
            print(f"ID: {node.id:2} | IP: {node.ip_address:12} | Status: {node.status}")

async def monitor_nodes():
    print("\n--- Запуск моніторингу вузлів... ---")
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Node))
        nodes = result.scalars().all()

        for node in nodes:
            await asyncio.sleep(0.1)
            last_octet = int(node.ip_address.split('.')[-1])
            node.status = "online" if last_octet % 2 != 0 else "offline"

        await session.commit()
    print("--- Моніторинг завершено ---")

async def main():
    await create_tables()
    await reset_nodes()
    await add_initial_nodes()

    await display_nodes("До оновлення")
    await monitor_nodes()
    await display_nodes("Після оновлення")


asyncio.run(main())