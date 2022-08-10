MAX_HASH_TABLE_SIZE = 4096

class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
    
    def get_index(self, key):
        # Use Python's in-built `hash` function and implement linear probing
        return hash(key) % len(self.data_list)
    
    
    def get_valid_index(self, key):
        idx = self.get_index(key)

        while True:
            # Get the key-value pair stored at idx
            kv = self.data_list[idx]

            # If it is None, return the index
            if kv is None:
                return idx

            # If the stored key matches the given key, return the index
            k, v = kv
            if k==key:
                return idx

            # Move to the next index
            idx += 1

            # Go back to the start if you have reached the end of the array
            if idx == len(self.data_list):
                idx = 0
        
    def __getitem__(self, key):
        # Implement the logic for "find" here
        
        # 1. Find the index for the key using get_valid_index
        idx = self.get_valid_index(key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
    
    def __setitem__(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = self.get_valid_index(key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key,value
        
        
    def __iter__(self):
        return (x for x in self.data_list if x is not None)
    
    def __len__(self):
        return len([x for x in self])
    
    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    
    def __str__(self):
        return repr(self)
