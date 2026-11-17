
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        previous = node.prev
        next_node = node.next

        previous.next = next_node
        next_node.prev = previous

    # Insert a node before tail (most recently used)
    def insert(self, node):
        previous = self.tail.prev

        previous.next = node
        node.prev = previous

        node.next = self.tail
        self.tail.prev = node

    # Get the value of a key
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    # Insert or update a key-value pair
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:

            least_used = self.head.next

            self.remove(least_used)

            del self.cache[least_used.key]
