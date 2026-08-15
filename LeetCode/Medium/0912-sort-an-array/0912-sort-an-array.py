class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums: List[int], left: int, right: int):
            if left >= right:
                return

            mid = left + (right - left) // 2

            mergeSort(nums, left, mid)
            mergeSort(nums, mid+1, right)

            merge(nums, left, right, mid)

        def merge(nums: List[int], left: int, right: int, mid: int):
            temp = []
            i, j = left, mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= right:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[left + k] = temp[k]

        mergeSort(nums, 0, len(nums) - 1)
        return nums
        