class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Find the min and max to know our range boundaries
        min_val = min(nums)
        max_val = max(nums)
        
        # Create a frequency array. 
        # Size is max - min + 1 to account for 0 and negative ranges.
        counts = [0] * (max_val - min_val + 1)
        
        # Tally the occurrences of each number
        for num in nums:
            counts[num - min_val] += 1
            
        # Reconstruct the sorted array
        index = 0
        for i in range(len(counts)):
            while counts[i] > 0:
                nums[index] = i + min_val
                index += 1
                counts[i] -= 1
                
        return nums