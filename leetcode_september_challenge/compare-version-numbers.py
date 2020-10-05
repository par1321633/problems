"""
https://leetcode.com/problems/compare-version-numbers/

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.


Example
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".


Input: version1 = "1.0.1", version2 = "1"
Output: 1


Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""

# !/usr/bin/env python
# -*- coding: utf-8
__author__ = "Parkash Sharma"


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        l1 = len(version1)
        l2 = len(version2)
        for i in range(min(l1, l2)):
            print(version1[i], version2[i])
            v1, v2 = version1[i].lstrip("0"), version2[i].lstrip("0")
            v1 = 0 if len(v1) == 0 else v1
            v2 = 0 if len(v2) == 0 else v2
            if int(v1) > int(v2):
                return 1
            elif int(v1) < int(v2):
                return -1
        if l1 > l2:
            for i in range(l2, l1):
                print(i)
                if int(version1[i]) > 0:
                    return 1
        else:
            for i in range(l1, l2):
                print(i)
                if int(version2[i]) > 0:
                    return -1
        return 0


if __name__ == '__main__':
    print("Running version comparison Program")

    version1 = "1.01"
    version2 = "1.001"
    print("Case 1 : version1 : {}, version2 : {}".format(version1, version2))
    sol = Solution().compareVersion(version1, version2)
    print("Solution : {}".format(sol))

    version1 = "1.0.1"
    version2 = "1"
    print("Case 2 : version1 : {}, version2 : {}".format(version1, version2))
    sol = Solution().compareVersion(version1, version2)
    print("Solution : {}".format(sol))

    version1 = "7.5.2.4"
    version2 = "7.5.3"
    print("Case 3 : version1 : {}, version2 : {}".format(version1, version2))
    sol = Solution().compareVersion(version1, version2)
    print("Solution : {}".format(sol))
