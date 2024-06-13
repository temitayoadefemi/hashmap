class ListNode():
    def __init__(self):
        self.key = None
        self.value = None
        self.next = None


class HashMap():
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * self.size


    def insert(self, key, value):
        hashpoint = self.hash(key, self.size)
        node = self.buckets[hashpoint]

        while node != None:
            if node.key == key:
                node.value = value
            
            node = node.next

        newnode = ListNode()
        newnode.key = key
        newnode.value = value
        newnode.next = self.buckets[hashpoint]
        self.buckets[hashpoint] = newnode

    
    def hash(self, key, size):
        # Example hash function: simple modulus based on size of buckets
        return hash(key) % size


    def __getitem__(self, key):
        hashpoint = self.hash(key, self.size)
        node = self.buckets[hashpoint]


        while node != None:
            if node.key == key:
                return node.value
            
            node = node.next

        return None
        