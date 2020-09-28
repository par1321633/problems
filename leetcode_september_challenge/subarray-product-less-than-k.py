"""
https://leetcode.com/problems/subarray-product-less-than-k/

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

"""
from typing import List

def check_val_recur(out, nums, val, backward_index, forward_index, limit):
    if forward_index > len(nums)-1:
        return out
    val = val * nums[forward_index]

    print (val, forward_index, backward_index)
    while val >= limit and backward_index < len(nums) -1 :
        print (backward_index)
        val = val // nums[backward_index]
        backward_index = backward_index + 1
    out = out + forward_index - backward_index + 1
    print ("OUTTT")
    print (out)
    return check_val_recur(out, nums, val, backward_index, forward_index=forward_index + 1, limit=limit)


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #print (nums, k)
        out = 0
        #for i in range(len(nums)):
            #print (nums[i])
            #check_val_recur(out, nums, val=1, index=i,limit=k)
        out = check_val_recur(out, nums, val=1, backward_index=0,  forward_index=0,limit=k)
        return out


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 0
    print ("Case 1 : Nums : {}, Limit : {}".format(nums, k))
    sol = Solution().numSubarrayProductLessThanK(nums, k)
    print ("Solution : {}".format(sol))

    nums = [10, 5, 2, 6]
    k = 100
    print("Case 2 : Nums : {}, Limit : {}".format(nums, k))
    sol = Solution().numSubarrayProductLessThanK(nums, k)
    print("Solution : {}".format(sol))
