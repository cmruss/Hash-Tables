
class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.entry_count = 0
        self.head = None

    def fnv1a(self, key):
        """
        FNV-1a 64-bit hash function
        Implement this, and/or DJB2.
        The FNV-1a hash differs from the FNV-1 hash 
        by only the order in which the multiply 
        and XOR is performed
        """
        # All variables, except for byte_of_data, are 64-bit unsigned integers
        # 64-bit FNV offset basis value (in hex, 0xcbf29ce484222325)
        fnv_offset_basis = 14695981039346656037
        # 64-bit FNV prime value (in hex, 0x100000001b3)
        fnv_prime = 1099511628211
        hash = fnv_offset_basis
        for b in key.encode():
            # XOR is an 8-bit operation that modifies only the lower 8-bits of the hash value
            hash = hash ^ b
            # multiply returns the lower 64-bits of the product.
            hash = hash * fnv_prime
        # The hash value returned is a 64-bit unsigned integer.
        return hash


    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        # Note that the starting value of the hash (5381) 
        # makes no difference for strings of equal lengths, 
        # but will play a role in generating different hash values
        # for strings of different lengths. 
        hash = 5381
        for b in key:
            # hash = 1448 + 5381 + each byte
            # << is the right bit shift operator
            hash = (( hash << 5) + hash) + ord(b)
        return hash # &= 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1a(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        index = self.hash_index(key)
        cur_entry = self.storage[index]
        new_entry = HashTableEntry(key, value)
    
        # if the index is None, overwite with new_entry
        if cur_entry is None:
            self.storage[index] = new_entry
            self.entry_count += 1
            # if the index is taken but shares a key, overwrite value
        elif cur_entry.key == key:
            cur_entry.value = value

        # --> LINKED LIST IMPLEMENTATION <--
        # else: # if we haven't specified a next this will be the first open next
        #     while cur_entry.next is not None:
        #         # for updating the next value in the linked list
        #         if cur_entry.next.key == key:
        #             cur_entry.next.value = value
        #         # move on to the next entry
        #         cur_entry = cur_entry.next
        #     # if we find an open next, tack it on as the next value
        #     cur_entry.next = HashTableEntry(key, value)
        # if we hit the load factor with the last addition, double size.

        # resize implementation
        if self.entry_count / self.capacity >= 0.7:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        if not index:
            print(f"No key found")
        else:
            self.entry_count -= 1
        self.storage[index] = None
        # if the load factor is enough reduced with our deletion
        # call resize to halve the size
        if self.entry_count / self.capacity <= 0.2:
            self.resize()

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        cur_entry = self.storage[index]

        if cur_entry is not None:
            return cur_entry.value
        else:
            return None
        
    def resize(self, capacity=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """
        prev_storage = self.storage
        # if the capacity is specified 
        # use that arg, unless less than 8
        if capacity is not None and capacity >= 8:
            self.capacity = capacity
        # if the proposed downsized capacity is not less than or equal to 8
        # and the load factor is equal to or less than 0.2
        # halve the capacity to a round number
        elif self.capacity / 2 >= 8 and self.entry_count / self.capacity <= 0.2:
            self.capacity = self.capacity // 2
        # if however the load factor is greater than 0.7
        # double the capacity
        elif self.entry_count / self.capacity >= 0.7:
            self.capacity = self.capacity * 2
        else: # if we meet none of our conditions, start with 8
            self.capacity = 8
        # create new storage
        self.storage = [None] * self.capacity
        # then reset the entry count
        self.entry_count = 0
        # add each entry that does not equal None
        for entry in prev_storage:
            if entry is not None:
                self.put(entry.key, entry.value)

    # def check_load(self):
    #     """
    #     Checks the current load factor
    #     by comparing not None values in 
    #     storage against total capacity
    #     """
    #     cur_storage = self.storage
    #     entry_count = 0
    #     for entry in cur_storage:
    #         if entry is not None:
    #             entry_count += 1
    #     self.load = entry_count / self.capacity

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")