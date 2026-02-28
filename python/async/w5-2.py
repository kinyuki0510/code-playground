import asyncio

async def task(name, seconds):
    print(f"{name} 開始")
    await asyncio.sleep(seconds)
    print(f"{name} 終了")
    return name

async def main():
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
    )
    print(results)

asyncio.run(main())