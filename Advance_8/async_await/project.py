import asyncio
import aiohttp


async def fetch(session, url):
    """
    Makes an async HTTP GET request and returns response text
    """
    # Send request (non-blocking)
    async with session.get(url) as res:
        # Wait for full response body (also non-blocking)
        return await res.text()


async def main():
    # List of URLs to fetch (same URL repeated 5 times)
    urls = ["https://example.com"] * 5

    # Create a single session (connection pooling → faster)
    async with aiohttp.ClientSession() as session:

        # Create tasks → start all requests immediately (concurrent)
        tasks = [asyncio.create_task(fetch(session, u)) for u in urls]

        # Process results as they complete (NOT in order)
        for task in asyncio.as_completed(tasks):

            # Wait for the next completed task
            result = await task

            # Print size of response
            print("Got response", len(result))


# Start event loop and run main coroutine
asyncio.run(main())