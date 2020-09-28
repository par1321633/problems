"""
https://leetcode.com/problems/sequential-digits/
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""

from typing import List

def generate_num_and_check(high, low, num,ones_digit, out):
    if num > high:
        return
    if ones_digit == 9:
        return
    if num >= low:
        out.append(num)
    ones_digit = int(str(num)[-1])
    num = int("{}{}".format(num, ones_digit+1))
    generate_num_and_check(high, low, num, ones_digit, out)


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        out = []
        for i in range(1,10):
            generate_num_and_check(high, low, i, i, out)
        return sorted(out)


if __name__ == '__main__':
    low = 100
    high = 300
    print ("Case 1 : Low {}, High {}".format(low, high))
    sol = Solution().sequentialDigits(low, high)
    print ("Solution : {}".format(sol))

    low = 1000
    high = 13000
    print("Case 2 : Low {}, High {}".format(low, high))
    sol = Solution().sequentialDigits(low, high)
    print("Solution : {}".format(sol))
