"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""

from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # print (A)
        # print (B)
        a_hash = {}
        b_hash = {}
        max_val_a = 0
        max_val_b = 0
        for i in range(len(A)):
            # print (A[i], B[i])
            if A[i] not in a_hash:
                a = self.check_swap_numbers(A, B, A[i])
                if a != -1:
                    a_hash[A[i]] = a
            if B[i] not in b_hash:
                b = self.check_swap_numbers(B, A, B[i])
                if b != -1:
                    b_hash[B[i]] = b
        # print (a_hash, b_hash)
        if len(a_hash) == 0 and len(b_hash) == 0:
            return -1
        a_min = min([val for i, val in a_hash.items()])
        b_min = min([val for i, val in b_hash.items()])
        return min(a_min, b_min)

    def check_swap_numbers(self, A, B, val):
        # print (A, B, val)
        swap_num = 0
        for i in range(len(A)):
            # print (A[i], B[i], val)
            if A[i] != val and B[i] != val:
                return -1
            elif A[i] != val and B[i] == val:
                swap_num = swap_num + 1
        return swap_num


if __name__ == '__main__':

    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]
    print ("Case 1 : A {}, B {}".format(A, B))
    sol = Solution().minDominoRotations(A, B)
    print ("Solution : {}".format(sol))

    A =  [3,5,1,2,3]
    B = [3,6,3,3,4]
    print("Case 2 : A {}, B {}".format(A, B))
    sol = Solution().minDominoRotations(A, B)
    print("Solution : {}".format(sol))

