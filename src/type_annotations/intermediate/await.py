"""
TODO:

`run_async` takes an awaitable integer.
"""

from typing import Awaitable
from asyncio import Queue


def run_async(_: Awaitable[int]) -> None:
    ...


if __name__ == "__main__":
    queue: Queue[int] = Queue()
    queue2: Queue[str] = Queue()


    async def async_function() -> int:
        return await queue.get()


    async def async_function2() -> str:
        return await queue2.get()


    run_async(async_function())
    run_async(1)  # type: ignore[arg-type]
    run_async(async_function2())  # type: ignore[arg-type]
