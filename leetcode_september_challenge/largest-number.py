"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

"""
from typing import List


def str_comparator(s1, s2):
    p, q = len(s1), len(s2)
    i = 0
    max_pq = 2 * max(p, q)
    while True:
        if i > max_pq:
            return False
        print(s1[i % p], s2[i % q])
        if s1[i % p] > s2[i % q]:
            return True
        elif s1[i % p] < s2[i % q]:
            return False
        i = i + 1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(i) for i in nums]
        for i in range(n - 1):
            for j in range(n - i - 1):
                if str_comparator(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(nums)
        return str(int(''.join(nums[::-1])))


if __name__ == '__main__':

    nums = [3,30,34,5,9]
    print ("CASE 1 : Nums : {}".format(nums))
    sol = Solution().largestNumber(nums)
    print ("Solution : {}".format(sol))

    nums =  [10,2]
    print("CASE 2 : Nums : {}".format(nums))
    sol = Solution().largestNumber(nums)
    print("Solution : {}".format(sol))

    nums =  [1,2,4,8,16,32,64,128,256,512]
    print("CASE 3 : Nums : {}".format(nums))
    sol = Solution().largestNumber(nums)
    print("Solution : {}".format(sol))