class LinearProbingHashmap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def find(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.size
        return False

    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def remove(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size

# Example usage:
hashmap = LinearProbingHashmap(10)
hashmap.insert("key1", "value1")
hashmap.insert("key2", "value2")
print(hashmap.find("key1"))  # True
print(hashmap.find("key3"))  # False
hashmap.remove("key1")
print(hashmap.find("key1"))  # False