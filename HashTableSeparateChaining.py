class HashTableSeparateChaining:
    def __init__(self, capacity=3, load_factor=0.75):
        if capacity <= 0 or load_factor <= 0 or load_factor == float("inf"):
            raise ValueError("Illegal capacity or load factor")
        self.capacity = capacity
        self.load_factor = load_factor
        self.size_ = 0
        self.buckets = [[] for _ in range(capacity)]
        self.mod_count = 0

    def clear(self):
        self.size_ = 0
        self.buckets = [[] for _ in range(self.capacity)]
        self.mod_count += 1

    def size(self):
        return self.size_

    def is_empty(self):
        return self.size_ == 0

    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.capacity

    def put(self, key, value):
        if key is None:
            raise ValueError("Null key")
        if self.size_ >= self.capacity * self.load_factor:
            self.resize()
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                old_val = v
                bucket[i] = (key, value)
                return old_val
        bucket.append((key, value))
        self.size_ += 1
        self.mod_count += 1
        return None

    def add(self, key, value):
        return self.put(key, value)

    def get(self, key):
        if key is None:
            return None
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for (k, v) in bucket:
            if k == key:
                return v
        return None

    def has_key(self, key):
        return self.contains_key(key)

    def contains_key(self, key):
        if key is None:
            return False
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for (k, _) in bucket:
            if k == key:
                return True
        return False

    def remove(self, key):
        if key is None:
            return None
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size_ -= 1
                self.mod_count += 1
                return v
        return None

    def keys(self):
        ks = []
        for bucket in self.buckets:
            for (k, _) in bucket:
                ks.append(k)
        return ks

    def resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size_ = 0
        for bucket in old_buckets:
            for (k, v) in bucket:
                self.put(k, v)

    def __iter__(self):
        expected_mod_count = self.mod_count
        for bucket in self.buckets:
            for (k, _) in bucket:
                if expected_mod_count != self.mod_count:
                    raise RuntimeError("Concurrent modification")
                yield k
