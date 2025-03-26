# 706. Design HashMap
# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
# Example 1:
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        # initialize 1000 blank nodes with default val -1 in case theyre not found
        self.map = [Node() for i in range(1000)]  
        
    def put(self, key: int, value: int) -> None:
        index = key % len(self.map)
        node = self.map[index]
        while node.next:  # traverse the linked list
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        # if loop exits, end of list has been reached, insert new node
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        index = key % len(self.map)
        node = self.map[index].next
        while node:  # traverse the linked list
            if node.key == key:
                return node.val
            node = node.next
        return -1  # if loop exits, key was not found, so return default val of -1

    def remove(self, key: int) -> None:
        index = key % len(self.map)
        node = self.map[index]
        while node and node.next:  # traverse the linked list
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next 
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
