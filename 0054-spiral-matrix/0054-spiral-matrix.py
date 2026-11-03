class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        res = []
        
        while left <= right and top <= bottom:
        
            # left -> right
            for i in range(left, right):
                res.append(matrix[top][i])

            top += 1

            # top -> bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])

            right -= 1

            if top >= bottom:
                break

            # right -> left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])

            bottom -= 1

            if left >= right:
                break

            # bottom -> top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])

            left += 1

            if (len(res) == len(matrix[0]) * len(matrix)):
                break

        return res

