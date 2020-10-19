"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

from copy import copy
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%len(nums)
        sol = copy(nums)
        print (k, l)
        print (sol)
        for i in range(l):
            print (i, i+k, (i+k)%l)
            nums[(i+k)%l] = sol[i]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print ("Case 1 : Nums {}, K {}".format(nums, k))
    sol = Solution().rotate(nums, k)
    print ("Solution : {}".format(sol))

    nums = [-1,-100,3,99]
    k = 2
    print("Case 2 : Nums {}, K {}".format(nums, k))
    sol = Solution().rotate(nums, k)
    print("Solution : {}".format(sol))

    nums =[1,2,3]
    k = 2
    print("Case 3 : Nums {}, K {}".format(nums, k))
    sol = Solution().rotate(nums, k)
    print("Solution : {}".format(sol))