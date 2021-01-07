"""
https://leetcode.com/problems/kth-missing-positive-number/

"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        print(arr, k, len(arr))
        range_req = k + len(arr)
        arr_input = [i for i in range(1, range_req + 1)]

        out = [i for i in arr_input if i not in arr]
        print(out)
        return out[k - 1]


if  __name__ == '__main__':
    print ("Running k-th missing positive number")

    arr = [1, 2, 3, 4]
    k = 2
    print("Case 1 : ARR {}, K : {}".format(arr, k))
    sol = Solution().findKthPositive(arr, k)
    print ("Solution : {}".format(sol))
    print("\n")

    arr = [2,3,4,7,11]
    k = 5
    print("Case 1 : ARR {}, K : {}".format(arr, k))
    sol = Solution().findKthPositive(arr, k)
    print ("Solution : {}".format(sol))
    print("\n")