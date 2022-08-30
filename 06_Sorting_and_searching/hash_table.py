from random import randint


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def get_hash(self, key, size):
        return key % size

    def rehash(self, old_hash, size, step):
        return (old_hash + step) % size

    def put(self, key, data):
        hash_value = self.get_hash(key, len(self.slots))

        # add key and data in empty slot
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # replace old data with current val
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, self.slots, 1)
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots), 1)

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.get_hash(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots), 1)
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hash_print(self):
        for i in range(len(self.slots)):
            print(f"<<{self.slots[i]} : {self.data[i]}>>")


h = HashTable()
keys = [randint(0, 11) for i in range(10)]
vals = [randint(0, 11) for i in range(10)]
print(keys, vals)
for i in range(9):
    h.put(keys[i], vals[i])
h.hash_print()
