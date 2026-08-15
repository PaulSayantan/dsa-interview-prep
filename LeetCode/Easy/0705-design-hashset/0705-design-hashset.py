"""
### Conceptual Breakdown

- Core Algorithmic Patterns: 
  Hashing, Array Manipulation, Collision Resolution (Separate Chaining).

- Mental Intuition & Logic:
  The goal of a HashSet is to provide average O(1) time complexity for additions, removals, 
  and lookups. Since we cannot use built-in sets, we must build the underlying mechanics:
  
  1. The Hash Function: We need to map a potentially large key space (up to 1,000,000) 
     into a smaller, manageable array (our "buckets"). We do this using the modulo operator 
     (`key % SIZE`). Choosing a prime number for `SIZE` (like 2069) helps distribute the keys 
     more evenly across the buckets, reducing collisions.
     
  2. Collision Resolution: Because the key space is larger than our number of buckets, 
     multiple keys will inevitably map to the same bucket (a collision). We handle this 
     using "Separate Chaining"—each bucket is not just a single value, but a secondary 
     data structure (like a Linked List or a dynamic array/list) that stores all keys 
     hashing to that specific index.
"""

class MyHashSet:
    """
    A custom implementation of a HashSet using a fixed-size array and separate chaining 
    for collision resolution.
    """

    def __init__(self):
        """
        Initializes the HashSet.
        
        We use a prime number (2069) for the base array size to reduce the clustering 
        of hashes and ensure a more uniform distribution of keys across the buckets.
        Each bucket is initialized as an empty list to handle potential collisions.
        """
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        """
        A private helper method to compute the hash value for a given key.
        
        Args:
            key (int): The element to be hashed.
            
        Returns:
            int: The mapped index for the bucket array.
        """
        return key % self.size

    def add(self, key: int) -> None:
        """
        Inserts the value key into the HashSet.
        
        Args:
            key (int): The element to add.
            
        Logic:
            1. Compute the bucket index using the hash function.
            2. Check if the key already exists in the bucket to maintain uniqueness.
            3. If it doesn't exist, append it to the bucket's list.
        """
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        """
        Removes the value key in the HashSet. If key does not exist, do nothing.
        
        Args:
            key (int): The element to remove.
            
        Logic:
            1. Compute the bucket index.
            2. Iterate through the bucket's list. If the key is found, remove it.
        """
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns whether the value key exists in the HashSet or not.
        
        Args:
            key (int): The element to search for.
            
        Returns:
            bool: True if the key exists, False otherwise.
            
        Logic:
            1. Compute the bucket index.
            2. Linearly scan the bucket's list to see if the key is present.
               Because of our hash distribution, this list will be very short, 
               keeping the time complexity near O(1).
        """
        index = self._hash(key)
        return key in self.buckets[index]


"""
### Reusable Patterns & Key Takeaways

1. Hash Function Design: 
   Using `key % prime_number` is a universally reusable pattern for mapping large 
   integer domains down to a smaller, fixed-size contiguous memory space (arrays). 

2. Separate Chaining for Collisions:
   Whenever you build a hash-based data structure (HashMap, HashSet), chaining 
   (using lists/linked lists inside array slots) is one of the safest and easiest 
   ways to resolve collisions without worrying about array resizing or complex 
   probing sequences.

3. Abstraction:
   By separating the `_hash(key)` logic into its own helper function, the `add`, 
   `remove`, and `contains` methods remain clean. This is an industry-standard 
   practice for building modular, easily refactorable classes.
"""