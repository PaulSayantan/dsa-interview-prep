class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem:
            Given an array of integers and a target value, return the indices
            of the two numbers such that they add up to the target.

        Approach: Hash Map (One-Pass)

        Intuition:
            For every number nums[i], we need another number:

                complement = target - nums[i]

            If we have already seen this complement earlier in the array,
            then we have found the required pair.

            To efficiently check whether the complement exists,
            we store previously visited numbers in a hash map:

                value -> index

            This allows O(1) average lookup time.

        Algorithm:
            1. Create an empty hash map.
            2. Traverse the array once.
            3. For each number:
                - Compute its complement.
                - If complement exists in the hash map:
                    return [index_of_complement, current_index]
                - Otherwise store the current number and its index.
            4. If no pair exists, return None.

        Example:
            nums   = [2, 7, 11, 15]
            target = 9

            i = 0, num = 2
            complement = 7
            Store {2: 0}

            i = 1, num = 7
            complement = 2
            2 already exists in map

            Return [0, 1]

        Time Complexity:
            O(n)
            Each element is processed once.

        Space Complexity:
            O(n)
            In the worst case, all elements are stored in the hash map.
        """

        # Stores:
        # number -> index
        hmap = {}

        # Traverse the array once
        for i in range(len(nums)):

            # Number required to reach the target
            complement = target - nums[i]

            # If complement was seen before,
            # we have found the answer
            if complement in hmap:
                return [hmap[complement], i]

            # Otherwise store the current number
            # for future complement lookups
            hmap[nums[i]] = i

        # No valid pair found
        return None
        