
class HashTable:
    def __init__(self, size):
        self.data = [[] for i in range(size)]

    def _hash(self, key):
        hash_value = 0
        for index, char in enumerate(key):
            hash_value = (hash_value + ord(char) * index) % len(self.data)
            # print(hash_value)
        return hash_value

    def get(self, key):
        address = self._hash(key)
        bucket = self.data[address]
        for key_value in bucket:
            if key_value[0] == key:
                return key_value[1]
        return None

    def set(self, key, value):
        address = self._hash(key)
        self.data[address].append((key, value))

    def keys(self):
        keys_array = []
        for bucket in enumerate(self.data):
            bucket_entries = bucket[1]
            keys_array += [key_value[0] for key_value in bucket_entries]
        return keys_array


if __name__ == "__main__":
    table = HashTable(1)
    table.set('grapes', 10000)
    table.set('apples', 99)
    print(table.get("grapes"))
    print(table.get("apples"))
    print(table.get("non existing"))

    table.set('oranges', 2)
    print(table.keys())
