from math import log2
from heapq import heappush, heappop

class Solution:
    def maxTotalValue(self, nums, k):

        n = len(nums)

        ####################################################
        # Build Sparse Tables
        ####################################################

        LOG = (n).bit_length()

        st_max = [[0] * LOG for _ in range(n)]
        st_min = [[0] * LOG for _ in range(n)]

        # length = 1
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]

        # Build larger powers of two
        j = 1
        while (1 << j) <= n:

            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):

                st_max[i][j] = max(
                    st_max[i][j - 1],
                    st_max[i + half][j - 1]
                )

                st_min[i][j] = min(
                    st_min[i][j - 1],
                    st_min[i + half][j - 1]
                )

            j += 1

        ####################################################
        # Range Query O(1)
        ####################################################
        def get_value(l, r):

            length = r - l + 1

            p = length.bit_length() - 1

            mx = max(
                st_max[l][p],
                st_max[r - (1 << p) + 1][p]
            )

            mn = min(
                st_min[l][p],
                st_min[r - (1 << p) + 1][p]
            )

            return mx - mn

        ####################################################
        # Max Heap
        ####################################################
        heap = []

        # start with largest interval for every left endpoint
        for l in range(n):

            r = n - 1

            value = get_value(l, r)

            # Python heap is min-heap
            heappush(heap, (-value, l, r))

        answer = 0

        ####################################################
        # Extract top k intervals
        ####################################################
        for _ in range(k):

            value, l, r = heappop(heap)

            value = -value

            answer += value

            # move one position left
            if r > l:

                new_r = r - 1

                new_value = get_value(l, new_r)

                heappush(
                    heap,
                    (-new_value, l, new_r)
                )

        return answer