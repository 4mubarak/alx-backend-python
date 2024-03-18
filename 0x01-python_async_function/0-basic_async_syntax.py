#!/usr/bin/env python3
'''Task 0's module.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    random_delay = await wait_random()
    print(f"Random delay: {random_delay} seconds")


asyncio.run(main())
