"""
https://leetcode.com/problems/remove-covered-intervals/

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.



Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
Example 3:

Input: intervals = [[0,10],[5,12]]
Output: 2
Example 4:

Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2
Example 5:

Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1


Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= intervals[i][0] < intervals[i][1] <= 10^5
All the intervals are unique.

"""

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed_items = 0
        intervals = (sorted(intervals))
        print (intervals)
        for i in range(1, len(intervals)):
            print (intervals[i])
            print (intervals[i-1][0], intervals[i][0] , intervals[i-1][1], intervals[i][1])
            if intervals[i-1][0] <= intervals[i][0] and intervals[i-1][1] >= intervals[i][1]:
                print ("NEED TO REMOVED")
                removed_items = removed_items + 1
                intervals[i] = intervals[i-1]
            elif intervals[i-1][0] >= intervals[i][0] and intervals[i-1][1] <= intervals[i][1]:
                print ("SECOND ONE IS BIGGER SET")
                removed_items = removed_items + 1
        return len(intervals) - removed_items


if __name__ == '__main__':
    intervals = [[1, 4], [3, 6], [2, 8]]
    print ("Case : Intervals {}".format(intervals))
    sol = Solution().removeCoveredIntervals(intervals)
    print ("Solution : {}".format(sol))

    intervals = [[1,4],[2,3]]
    print("Case : Intervals {}".format(intervals))
    sol = Solution().removeCoveredIntervals(intervals)
    print("Solution : {}".format(sol))

    intervals = [[0,10],[5,12]]
    print("Case : Intervals {}".format(intervals))
    sol = Solution().removeCoveredIntervals(intervals)
    print("Solution : {}".format(sol))

    intervals =  [[3,10],[4,10],[5,11]]
    print("Case : Intervals {}".format(intervals))
    sol = Solution().removeCoveredIntervals(intervals)
    print("Solution : {}".format(sol))