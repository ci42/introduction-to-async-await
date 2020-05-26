import asyncio
import time

from unsync import unsync

def cpu_intensive_task():
    for _ in range(1, 300_000_000):
        pass

@unsync()
def synchronous_thread():
    time.sleep(5)
    return "synchronous_thread completed!"

@unsync(cpu_bound=True)
def synchronous_process():
    cpu_intensive_task()
    return "synchronous_process completed!"


@unsync
async def asynchronous():
    await asyncio.sleep(5)
    return "asynchronous completed!"
