import math
import random

def lookup_table():
    for i in range(1,50000):
        slowfun(i, i+1)

def slowfun(x, y, cache={}):
    # TODO: Modify to produce the same results, but much faster
    if cache.get(f"{x},{y}"):
        return cache[f"{x},{y}"]
    else:
        v = math.pow(x, y)
        # v = math.factorial(v)
        """ ^ is crashing Python?
        but the following expression is equivalent
        at least for time complexity (I hope)"""
        factorial = v
        for i in range(1, round(v)+1):
            factorial *= v
        v = factorial
        v //= (x + y)
        v %= 982451653

        cache[f"{x},{y}"] = v

    return cache[f"{x},{y}"]

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
