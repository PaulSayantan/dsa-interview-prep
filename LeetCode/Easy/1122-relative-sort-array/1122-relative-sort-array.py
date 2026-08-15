class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = 0
        for j in range(len(arr2)):
            for k in range(i, len(arr1)):
                print(i, j, k)
                if arr1[k] == arr2[j]:
                    print("old nums: ", arr1)
                    arr1[i], arr1[k] = arr1[k], arr1[i]
                    i += 1
                    print("updated nums: ", arr1)
            print("now nums: ", arr1)

        # rest of the elements of arr1 needs to be sorted
        arr1[i::] = sorted(arr1[i::])
        
        return arr1