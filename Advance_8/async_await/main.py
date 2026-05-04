# Normal Python runs one task at a time:

import time


# def task():
#     print("Start")
#     time.sleep(3)   # blocks everything
#     print("End")

# task()

# Async = don’t wait idly → do something else meanwhile

# Think:

# “Start task → pause → do other work → resume later”

# async def → defines async function (coroutine)
# await → pause here, let other tasks run
# asyncio.sleep() → non-blocking sleep




import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} finished")

# async def main():
#     await asyncio.gather(
#         task("A"),
#         task("B"),
#         task("C")
#     )


async def main():
    t1 = asyncio.create_task(task("A"))
    t2 = asyncio.create_task(task("B")) 

    await t1
    await t2

asyncio.run(main())


# Python uses event loop
# Tasks are paused & resumed
# No real threads → just smart scheduling


# | Method                         | Behavior     |
# | ------------------------------ | ------------ |
# | `await task(A); await task(B)` | sequential ❌ |
# | `gather(A, B)`                 | concurrent ✅ |
# | `create_task + await`          | concurrent ✅ |

# Simple parallel tasks → use gather
# Need control / cancel / manage → use create_task

# try → risky code
# except → handle error
# finally → always run