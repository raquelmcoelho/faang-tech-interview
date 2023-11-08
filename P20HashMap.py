'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/mEpm8qvEyvG
Solution: Design HashMap

Design a hash map without using the built-in hash libraries. We only need to cater to integer keys and values in the hash map. Return NULL if the key doesn’t exist.

It should support the following three primary functions of a hash map:

Put(key, value): This function inserts a key and value pair into the hash map. If the key is already present in the map, then the value is updated accordingly.
Get(key): This function returns the value to which the key is mapped. It returns -1 if no mapping for the key exists.
Remove(key): This function removes the key and its mapped value.

Time complexity
The time complexity bounds of each hash map operations are given below in terms of n, the number of key-value pairs in the hash map:
Put():  The average-case complexity is O(1), while the worst-case complexity is O(n).
Get():  The average-case complexity is O(1), while the worst-case complexity is O(n).
Remove():  The average-case complexity is O(1), while the worst-case complexity is O(n).

Space complexity
The space required for this data structure is the sum of the size of the hash map, m, and the number of existing key-value pairs, n. So, the space complexity would be O(m+n).

'''

# A class implementation of the bucket data structure
class Bucket:
    # Initialize bucket here
    def __init__(self):
        self.bucket = []

    # get value from bucket
    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    # put value in bucket
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    # delete value from bucket
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap():
    # Initialize hash map here
    def __init__(self, key_space):
        # It’s better to have a prime number, so there's less collision
        self.key_space = key_space
        self.buckets = [Bucket() for i in range(self.key_space)]

    # Function to add value of a given key
    # hash map at the relevant hash address
    def put(self, key, value):
        if key== None or value == None:
            return
            
        hash_key = key % self.key_space
        self.buckets[hash_key].update(key, value)

    # Function to fetch corresponding value of a given key
    def get(self, key):
        if key == None:
            return -1
        hash_key = key % self.key_space
        return self.buckets[hash_key].get(key)

    # Function to remove corresponding value of a given key
    def remove(self, key):
        hash_key = key % self.key_space
        self.buckets[hash_key].remove(key)


# Driver code
def main():
    key_space = 11
    # Creating a hash map of size 11
    input_hash_map = MyHashMap(key_space)
    keys = [5, 11, 12, 15, 22, 10]
    keys_list = [5, 11, 12, 15, 22, 10]
    values = [100, 200, 400, 500, 1000, 5000]
    funcs = ["Get", "Get", "Put", "Get",
             "Put", "Get", "Get", "Remove",
             "Get", "Get", "Remove", "Get"]
    func_keys = [[5], [15], [15, 250], [15], 
                 [121, 110], [121], [10], [11], [11],
                 [13], [13], [None]]

    for i in range(len(keys)):
        input_hash_map.put(keys[i], values[i])

    for i in range(len(funcs)):
        if funcs[i] == "Put":
            print(
                i + 1,  ".\t put(", func_keys[i][0],  ", ", func_keys[i][1],  ")", sep="")
            if not func_keys[i][0] in keys_list:
                keys_list.append(func_keys[i][0])
            input_hash_map.put(func_keys[i][0], func_keys[i][1])
        elif funcs[i] == "Get":
            print(i + 1, ".\t get(", func_keys[i][0], ")", sep="")
            print("\t Value returned: ", input_hash_map.get(
                func_keys[i][0]), sep="")
        elif funcs[i] == "Remove":
            print(i + 1,  ". \t remove(", func_keys[i][0], ")", sep="")
            input_hash_map.remove(func_keys[i][0])

        # Printing the hashmap using our custom print function
        print("\nHash map:\n")
        #hash_print(input_hash_map, keys_list)
        print("-"*100)


if __name__ == '__main__':
    main()