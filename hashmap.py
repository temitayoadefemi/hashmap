class HashMap:
    """A simple implementation of a hash map using lists for buckets."""

    def __init__(self, size):
        """
        Initializes the hash map with a specified size.

        Args:
            size: The number of buckets in the hash map.
        """
        self.size = size  # Store the size for use in the hash function and bucket access
        self.buckets = [[] for _ in range(self.size)]  # Create empty lists for each bucket

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if not found.
        """
        hashpoint = self.hash(key)  # Calculate the bucket index using the hash function
        bucket = self.buckets[hashpoint] # Access the correct bucket
        for k, v in bucket:  # Iterate through key-value pairs in the bucket
            if k == key:
                return v  # Return the value if the key matches
        return None  # Key not found in the bucket

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash map. If the key already exists, updates the value.

        Args:
            key: The key to insert or update.
            value: The value to associate with the key.
        """
        hashpoint = self.hash(key)
        bucket = self.buckets[hashpoint]

        for i, (k, _) in enumerate(bucket):  # Check for existing key in bucket
            if k == key:
                bucket[i] = (key, value)  # Update the value if key exists
                return  # Exit the function to avoid appending again

        bucket.append((key, value))  # Append a new key-value pair to the bucket

    def hash(self, key):
        """
        Calculates the hash value for a given key.

        Args:
            key: The key to hash.

        Returns:
            The hash value, which is an integer within the range of bucket indices.
        """
        return hash(key) % self.size  # Use Python's built-in hash function and modulo operator



