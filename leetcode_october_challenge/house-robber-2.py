"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        return max(self.check_rob_sol(nums, 0, l - 1), self.check_rob_sol(nums, 1, l))

    def check_rob_sol(self, nums, start, end):
        A = 0
        B = 0
        for i in range(start, end):
            if i % 2 == 0:
                A = A + nums[i]
                A = max(A, B)
            else:
                B = B + nums[i]
                B = max(A, B)
        return max(A, B)


if __name__ == '__main__':
    nums = [1,2,1,1]
    print ("Case 1 : Nums {}".format(nums))
    sol = Solution().rob(nums)
    print ("Solution : {}".format(sol))

    nums = [2,1,1,2]
    print("Case 2 : Nums {}".format(nums))
    sol = Solution().rob(nums)
    print("Solution : {}".format(sol))

    nums = [1,2]
    print("Case 3 : Nums {}".format(nums))
    sol = Solution().rob(nums)
    print("Solution : {}".format(sol))