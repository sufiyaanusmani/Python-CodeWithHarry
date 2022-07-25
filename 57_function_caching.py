import time
from functools import lru_cache


@lru_cache(maxsize=3)  # stores last n calls
def someWork(n):
    # some task taking n seconds
    time.sleep(n)
    return n


if __name__ == "__main__":
    print("Now running some work")
    someWork(3)
    print("Done")
    someWork(3)
    print("Called again")
