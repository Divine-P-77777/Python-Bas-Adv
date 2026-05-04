from functools import lru_cache
import time


@lru_cache(maxsize=None)   # Cache all results (no limit)
def fx(n):
    time.sleep(5)          # Simulates heavy computation
    return n * 5


print(fx(20))
print("done for 20")

print(fx(2))
print("done for 2")

print(fx(6))
print("done for 6")

print(fx(20))   # This will be instant (cached)


print(fx.cache_info())

fx.cache_clear()  # Removes all stored values


# When to use

# Expensive computations
#  Recursive problems (like Fibonacci)
#  API calls / repeated inputs