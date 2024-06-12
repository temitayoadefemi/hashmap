
class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]
        

    def __getitem__(self, key):
        hashpoint = self.hash(key)
        bucket = self.buckets[hashpoint]
        for k, v in bucket:
            if k == key:
                return v
        

    def insert(self, key, value):
        hashpoint = self.hash(key)
        bucket = self.buckets[hashpoint]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))


    def hash(self, key):
        return hash(key) % self.size
        
        



