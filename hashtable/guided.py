hash_table_size = 10
hash_table = [None] * hash_table_size

def myhash(s):
    str_bytes = s.encode()
    total = 0
    for b in str_bytes:
        total +=b
    
    total &= 0xffffffff # 32-bit (8 figures)
    total &= 0xffffffffffffffff # 64-bit (16 figures)

    return total
    
def hash_index(s):
    h = myhash(s)

    return h % hash_table_size

def put(key, value):
    index = hash_index(key)
    hash_table[index] = value

def get(key):
    index = hash_index(key)
    return hash_table[index]

def delete(key):
    index = hash_index(key)
    hash_table[index] = None

if __name__ == "__main__": 
    """
    this method ensures that the below code only runs 
    when we call it in the CLI and not on import
    """

    # print(hash_index("Hello"))
    # print(hash_index("foobar"))
    # print(hash_index("cats"))
    # print(hash_index("cody"))
    # print(hash_index("foobaz")) # collision
    # print(hash_index("qux")) # collision

    print(hash_table)
    put("Hello", 37)
    put("foobar", 128)
    put("cats", "dogs")
    print(hash_table)
    print(get("Hello"))
    print(get("cody"))
    print(get("qux"))
    delete("Hello")
    print(hash_table)
elif __name__ == "guided":
    print("I've been imported")

# --> DAY 3 COLLISIONS CONTINUED <--

# --> BIRTHDAY PARADOX <--

import hashlib
import random

def hash_function(key):
    """
    Hashing function
    ​
    Low 32 bits of an MD5 hash
    """

    # You don't need to understand this line, but give it a shot anyway
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff

def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0

        tried = {}

        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets

            if index not in tried:
                tried[index] = True
                tries += 1
            else:
                break
        print(f'{buckets} buckets, {tries} hashes before collision. ({tries / buckets * 100:.1f}% full)')

how_many_before_collision(131072, 10)

# --> DAY 4  APPLICATIONS <--

# --> CACHING <--
"""
Slow calculation caching
100 -> 99th 98th
99 -> 98th 97th
98 -> 97th 96th
... 
computing lots of duplicates 
without a cache, it's very costly
"""

def fib(n, cache={}):
    if n<=1:
        return n

    if n not in cache:
        cache[n] = fib(n-1)+ fib(n-2)
    return cache[n]

print(fib(100))



# --> LOOKUP TABLE <--
"""
similiar problem
uses lookup_table to get the values added to the cache
so future calls will be faster 
"""

import math

def build_lookup_table():
    for i in range(1,1000):
        inv_square_root(i)

def inv_square_root(n, cache={}):
    cache[n] = 1 / math.sqrt(n)

    return cache[n]

for i in range(1, 6):
    print(inv_square_root(i))

# --> SORTING <--
""" 
dictionaries in python are unsorted, 
there exisits no sort attributes on them
but they do maintain a constant order;
to sort we can convert the dict
in this instance to a list of tuples
"""

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

items = list(d.items())
print(f"unsorted: {items}")

items.sort() # <-- sorts by key
print(f"sorted by key: {items}")

items.sort(key=lambda e: e[1], reverse=True) # <-- sorts by value, can reverse sort
print(f"reverse sort by value: {items}")

def get_key(e): # <-- also sorts by value
    return e[1]
items.sort(key=get_key)
print(f"sorted by value:")
for i in items:
    print(f"{i[0]}: {i[1]}")

sorted_d = dict(items)
print(f"sorted by value dictionary: {sorted_d} ")

# --> CAESAR CIPHER <--

encode_table = {

}

decode_table = {}

for k, v in encode_table.items():
    decode_table[v] = k

def encode(s):
    r = ""
    for c in s:
        r += encode_table[c]
    return r

def decode(s):
    r = ""