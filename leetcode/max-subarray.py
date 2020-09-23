"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [-2147483647]
Output: -2147483647

"""

from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        resum = 0
        print (nums)
        for i in nums:
            #sum2 = sum2 + i
            if resum + i  < i:
                resum = i
            else:
                resum = resum + i
            max_sum = max(max_sum, resum)
            print (i, max_sum, resum)
            print ("#######")
        return max_sum


if __name__ == '__main__':

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print ("CASE 1 : Nums : {}".format(nums))
    sol = Solution().maxSubArray(nums)
    print ("Solution : {}".format(sol))

    nums = [1,2]
    print("CASE 2 : Nums : {}".format(nums))
    sol = Solution().maxSubArray(nums)
    print("Solution : {}".format(sol))

    nums = [-1]
    print("CASE 3 : Nums : {}".format(nums))
    sol = Solution().maxSubArray(nums)
    print("Solution : {}".format(sol))