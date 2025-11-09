
# 1️⃣3️⃣ Async / Await

# Handle many I/O tasks at once (APIs, DB, file).

import asyncio

async def work():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(work())


# Multiple tasks:

async def run_all():
    await asyncio.gather(work(), work(), work())

asyncio.run(run_all())
