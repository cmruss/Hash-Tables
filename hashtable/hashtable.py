
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
        self.head = None

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """        

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """

        hash = 5381
        for b in key:
            hash = (( hash << 5) + hash) + ord(b)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

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
        # if the index is taken but shares a key, overwrite value
        elif cur_entry.key == key:
            cur_entry.value = value
        else: # else loop through storage comparing the current entry's next key
            while cur_entry.next is not None:
                # next values must also be updated
                if cur_entry.next.key == key:
                    cur_entry.next.value = value
                # move on to the next entry
                cur_entry = cur_entry.next
            # if we don't find anything, tack it on the end
            cur_entry.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        if not index:
            print(f"No key found")
        self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        cur_entry = self.storage[index]

        if cur_entry is not None:
            # loop through the hash table's entry keys
            while cur_entry.key != key:
                # if we find the key return the value
                if cur_entry.key == key:
                    return cur_entry.value
                else:
                    # move on to the next entry
                    cur_entry = cur_entry.next
            return cur_entry.value
        
    
        
    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

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