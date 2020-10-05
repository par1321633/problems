"""
https://leetcode.com/problems/insert-interval/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        out = []
        flag = False
        for i in intervals:
            if i[0] > newInterval[1] and flag is False:
                out.append(newInterval)
                flag = True

            if i[0] > newInterval[1]:
                out.append(i)
            elif i[1] < newInterval[0]:
                out.append(i)
            else:
                self.compute_req_interval(i, newInterval, out)
                flag = True

        if not flag:
            if intervals[0][0] > newInterval[1]:
                out.insert(0, newInterval)
            else:
                out.append(newInterval)
        return out

    def compute_req_interval(self, interval, new_interval, out):
        rmin = new_interval[0] if new_interval[0] < interval[0] else interval[0]
        rmax = interval[1] if interval[1] >= new_interval[1] else interval[1] if interval[1] < new_interval[0] else \
        new_interval[1]
        if len(out) > 0:
            last_interval = out[-1]
            if last_interval[1] < rmin:
                out.append([rmin, rmax])

            elif last_interval[0] <= rmin and last_interval[1] >= rmax:
                return
            elif last_interval[0] <= rmin and last_interval[1] < rmax:
                out[-1] = [last_interval[0], rmax]
                return
        else:
            out.append([rmin, rmax])



if __name__ == '__main__':
    print("Running version comparison Program")

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print("Case 1 : intervals : {}, newInterval : {}".format(intervals, newInterval))
    sol = Solution().insert(intervals, newInterval)
    print("Solution : {}".format(sol))

    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print("Case 2 : intervals : {}, newInterval : {}".format(intervals, newInterval))
    sol = Solution().insert(intervals, newInterval)
    print("Solution : {}".format(sol))

    intervals = [[1, 5]]
    newInterval = [0, 3]
    print("Case 3 : intervals : {}, newInterval : {}".format(intervals, newInterval))
    sol = Solution().insert(intervals, newInterval)
    print("Solution : {}".format(sol))

    intervals = [[0, 0], [1, 4], [6, 8], [9, 11]]
    newInterval = [0, 9]
    print("Case 4 : intervals : {}, newInterval : {}".format(intervals, newInterval))
    sol = Solution().insert(intervals, newInterval)
    print("Solution : {}".format(sol))

    intervals = [[1, 5]]
    newInterval = [0, 0]
    print("Case 5 : intervals : {}, newInterval : {}".format(intervals, newInterval))
    sol = Solution().insert(intervals, newInterval)
    print("Solution : {}".format(sol))