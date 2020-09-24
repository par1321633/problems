"""
https://leetcode.com/problems/spiral-matrix/
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

from typing import List


class Solution:
    def __init__(self, matrix=None):
        self.matrix = matrix
        self.movement = ['R', 'D', 'L', 'U']
        self.out = []

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []

        if matrix:
            self.matrix = matrix

        start_row = 0
        start_col = 0
        end_row = len(matrix) - 1
        end_col = len(matrix[0]) - 1
        self.spiral_traverse_matrix(0, start_row, start_col, end_row, end_col)
        return self.out

    def spiral_traverse_matrix(self, index, start_row, start_col, end_row, end_col):
        # print (matrix, index, start_row, start_col, end_row, end_col)
        # print (start_row >= end_row)
        # print (start_col >= end_col)

        if end_row < 0 or end_col < 0:
            return

        if start_row > end_row or start_col > end_col:
            return

        op = self.movement[index % len(self.movement)]
        # print (op)

        if op == 'R':
            for i in range(start_col, end_col + 1):
                # print (self.matrix[start_row][i])
                self.out.append(self.matrix[start_row][i])
            return self.spiral_traverse_matrix(index + 1, start_row + 1, start_col, end_row, end_col)

        elif op == 'D':
            for i in range(start_row, end_row + 1):
                # print (matrix[i][end_col])
                self.out.append(self.matrix[i][end_col])
            return self.spiral_traverse_matrix(index + 1, start_row, start_col, end_row, end_col - 1)

        elif op == 'L':
            for i in range(end_col, start_col - 1, -1):
                # print (matrix[end_row][i])
                self.out.append(self.matrix[end_row][i])
            return self.spiral_traverse_matrix(index + 1, start_row, start_col, end_row - 1, end_col)

        elif op == 'U':
            for i in range(end_row, start_row - 1, -1):
                # print (self.matrix[i][start_col])
                self.out.append(self.matrix[i][start_col])
            return self.spiral_traverse_matrix(index + 1, start_row, start_col + 1, end_row, end_col)


if __name__ == '__main__':

    matrix = [[6,9,7]]
    print ("CASE 1 : Matrix : {}".format(matrix))
    sol = Solution().spiralOrder(matrix)
    print ("Solution : {}".format(sol))

    matrix = []
    print("CASE 2 : Matrix : {}".format(matrix))
    sol = Solution().spiralOrder(matrix)
    print("Solution : {}".format(sol))

    matrix = [[1]]
    print("CASE 3 : Matrix : {}".format(matrix))
    sol = Solution().spiralOrder(matrix)
    print("Solution : {}".format(sol))

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print("CASE 4 : Matrix : {}".format(matrix))
    sol = Solution().spiralOrder(matrix)
    print("Solution : {}".format(sol))

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("CASE 5 : Matrix : {}".format(matrix))
    sol = Solution().spiralOrder(matrix)
    print("Solution : {}".format(sol))
