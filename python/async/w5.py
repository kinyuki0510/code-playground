import asyncio


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
async def fetch_user():
    await asyncio.sleep(2)
    return "Alice"

@log_decorator
async def fetch_order():
    await asyncio.sleep(2)
    return "Order"

async def main():
    # 同時に実行
    user, order = await asyncio.gather(
        fetch_user(),
        fetch_order()
    )
    print(user, order)


asyncio.run(main())