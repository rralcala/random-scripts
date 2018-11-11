import unittest

'''https://leetcode.com/problems/design-hashmap/'''


class MyNode:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}, {self.value}"


class MyHashMap:
    LIST_SIZE = 50000

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = [None] * self.LIST_SIZE

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        h = hash(key) % self.LIST_SIZE
        if self.store[h]:
            matches = [elem for elem in self.store[h] if elem.key == key]
            if matches:
                matches[0].value = value
                return
            else:
                self.store[h].append(MyNode(key, value))
        else:
            self.store[h] = [MyNode(key, value)]

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        h = hash(key) % self.LIST_SIZE
        if not self.store[h]:
            return -1
        matches = [elem for elem in self.store[h] if elem.key == key]
        if matches:
            return matches[0].value
        else:
            return -1

    def debug(self):

        for elem in self.store:
            print([str(x) for x in elem])

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        h = hash(key) % self.LIST_SIZE
        if self.store[h]:
            matches = [i for i in range(len(self.store[h])) if self.store[h] and self.store[h][i] and self.store[h][i].key == key]
            if matches:
                del self.store[h][matches[0]]


class Tests(unittest.TestCase):
    def test_examples(self):
        o = MyHashMap()
        c = ["remove", "get", "put", "put", "put", "get", "put", "put", "put", "put"]
        v = [[14], [4], [7, 3], [11, 1], [12, 1], [7], [1, 19], [0, 3], [1, 8], [2, 6]]
        results = []
        for i in range(len(c)):
            method_to_call = getattr(o, c[i])
            results.append(method_to_call(*v[i]))
        self.assertEqual(results, [None,-1,None,None,None,3,None,None,None,None])


if __name__ == "__main__":
    unittest.main()
