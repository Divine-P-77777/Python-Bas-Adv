import asyncio
import aiohttp


async def fetch(session, url):
    """
    Makes an async HTTP request and safely handles errors
    """
    try:
        # Try to send request
        async with session.get(url) as res:

            # Raise error for bad status (like 404, 500)
            res.raise_for_status()

            # Read response body (non-blocking)
            return await res.text()

    except aiohttp.ClientError as e:
        # Handles network / HTTP related errors
        print(f"Request failed: {e}")
        return None

    finally:
        # Always runs (success or error)
        print(f"Finished attempt for {url}")


async def main():
    urls = ["https://example.com"] * 5

    async with aiohttp.ClientSession() as session:

        # Start all tasks concurrently
        tasks = [asyncio.create_task(fetch(session, u)) for u in urls]

        # Process results as they complete
        for task in asyncio.as_completed(tasks):
            try:
                result = await task

                if result:
                    print("Got response", len(result))

            except Exception as e:
                # Catch unexpected errors from task
                print("Unexpected error:", e)

    # Example of normal try-except-finally (sync)
    try:
        x = 5 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Done")


# Run program
asyncio.run(main())