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
                node.value == value
            
            node = node.next

        newnode = ListNode()
        newnode.key = key
        newnode.value = value
        newnode.next = self.buckets[hashpoint]
        self.buckets[hashpoint] = newnode



    def __getitem___(self, key):
        hashpoint = self.hash(key, self.size)
        node = self.buckets[hashpoint]


        while node != None:
            if node.key == key:
                return node.value
            
            node = node.next

        return None
        