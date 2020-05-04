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
    # this method ensures that the below code only runs 
    # when we call it in the CLI and not on import

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
