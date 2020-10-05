"""
https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.


Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Input: nums = [2,1,1,2]
Output: 4
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        a = 0
        b = 0

        for i in range(len(nums)):
            if (i % 2 == 0):
                b = b + nums[i]
                b = max(a, b)
            else:
                a = a + nums[i]
                a = max(a, b)

        return max(a, b)


if __name__ == '__main__':
    print("Running version comparison Program")

    nums = [2,7,9,3,1]
    print("Case 1 : nums : {}".format(nums))
    sol = Solution().rob(nums)
    print("Solution : {}".format(sol))

    nums = [1, 2, 3, 1]
    print("Case 2 : nums : {}".format(nums))
    sol = Solution().rob(nums)
    print("Solution : {}".format(sol))

    nums = [2, 1, 1, 2]
    print("Case 3 : nums : {}".format(nums))
    sol = Solution().rob(nums)
    print("Solution : {}".format(sol))
