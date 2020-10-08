"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target

        def binary_search(start, end):
            print(start, end)
            if start >= end:
                return -1
            mid = (start + end) // 2
            if self.nums[mid] == self.target:
                return mid
            elif self.nums[mid] > self.target:
                return binary_search(start, mid)
            elif self.nums[mid] < self.target:
                return binary_search(mid + 1, end)
        return binary_search(0, len(nums))


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print ("Case 1 : Nums {}, Target {}".format(nums, target))
    sol = Solution().search(nums, target)
    print ("Solution : {}".format(sol))

    nums = [-1,0,3,5,9,12]
    target = 2
    print("Case 2 : Nums {}, Target {}".format(nums, target))
    sol = Solution().search(nums, target)
    print("Solution : {}".format(sol))

    nums = [5]
    target = 5
    print("Case 3 : Nums {}, Target {}".format(nums, target))
    sol = Solution().search(nums, target)
    print("Solution : {}".format(sol))
