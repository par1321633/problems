"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        for i in range(len(matrix)):
            print(matrix[i], i, matrix[i - 1])
            if len(matrix[i]) == 0:
                continue
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                return self.searchArray(matrix[i], target)
        return False

    def searchArray(self, array, target):
        if len(array) == 0:
            return False
        print(array, target)
        start = 0
        end = len(array)
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            return self.searchArray(array[start:mid], target)
        else:
            return self.searchArray(array[mid + 1:end], target)

if __name__ == '__main__':
    matrix = [[1]]
    target = 1
    print ("Case 1 : Matrix : {}, Target {}".format(matrix, target))
    sol = Solution().searchMatrix(matrix, target)
    print ("Solution : {}".format(sol))

    matrix = [[1,3]]
    target = 3
    print("Case 2 : Matrix : {}, Target {}".format(matrix, target))
    sol = Solution().searchMatrix(matrix, target)
    print("Solution : {}".format(sol))

    matrix =  [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 1
    print("Case 3 : Matrix : {}, Target {}".format(matrix, target))
    sol = Solution().searchMatrix(matrix, target)
    print("Solution : {}".format(sol))

