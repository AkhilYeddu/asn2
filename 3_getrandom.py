class RandomizedSet:
    def __init__(self):
        self.v = []
        self.mp = {}
        self.seed = 1  # Initialize seed for randomness

    def search(self, val: int) -> bool:
        return val in self.mp

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        
        self.v.append(val)
        self.mp[val] = len(self.v) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        
        index = self.mp[val]
        last_val = self.v[-1]
        
        self.v[index] = last_val
        self.mp[last_val] = index
        
        self.v.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        if not self.v:
            return None  # Handle empty case
        
        n = len(self.v)
        self.seed = (self.seed * 9301 + 49297) % 233280
        random_index = self.seed % n
        
        return self.v[random_index]
