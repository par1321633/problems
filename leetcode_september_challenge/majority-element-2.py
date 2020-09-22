"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
Input: [3,2,3]
Output: [3]


Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        required_obr = len(nums) / 3
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return [index for index, val in hash_map.items() if val > required_obr]


class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            print("############")
            print(n)
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
            print(candidate1, candidate2)
            print(count1, count2)

        print(candidate1, candidate2)
        print(count1, count2)
        # 2nd pass
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)

        return result


if __name__ == '__main__':
    nums = [3, 2, 3]
    print("CASE 1 : {}".format(nums))
    sol = Solution().majorityElement(nums)
    print("Solution : {}".format(sol))

    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print("CASE 2 : {}".format(nums))
    sol = Solution().majorityElement(nums)
    print("Solution : {}".format(sol))
