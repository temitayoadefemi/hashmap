class ListNode():
    # Node class to store a single key-value pair and a reference to the next node in the chain
    def __init__(self):
        self.key = None    # Key of the node
        self.value = None  # Value of the node
        self.next = None   # Pointer to the next node in the linked list


class HashMap():
    # Hash map class using separate chaining to handle collisions
    def __init__(self, size):
        self.size = size  # Number of buckets in the hash map
        self.buckets = [None] * self.size  # Initialize buckets with None

    def insert(self, key, value):
        # Calculates the bucket index and inserts the key-value pair
        hashpoint = self.hash(key, self.size)  # Get the bucket index
        node = self.buckets[hashpoint]  # Start with the head node in the bucket

        # Iterate over the linked list in the current bucket
        while node is not None:
            if node.key == key:
                node.value = value  # Update the value if the key is found
                return
            node = node.next  # Move to the next node in the list

        # If key not found, create a new node and add it at the beginning of the list
        newnode = ListNode()
        newnode.key = key
        newnode.value = value
        newnode.next = self.buckets[hashpoint]  # Point new node's next to the old head node
        self.buckets[hashpoint] = newnode  # Set new node as the new head of the list

    def hash(self, key, size):
        # Simple hash function using modulus to compute bucket index
        return hash(key) % size

    def __getitem__(self, key):
        # Retrieve the value for a given key in the hash map
        hashpoint = self.hash(key, self.size)  # Get the bucket index
        node = self.buckets[hashpoint]  # Start with the head node in the bucket

        # Iterate over the linked list in the current bucket
        while node is not None:
            if node.key == key:
                return node.value  # Return the value if the key is found
            node = node.next  # Move to the next node in the list

        return None  # Return None if the key is not found
