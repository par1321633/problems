"""
https://leetcode.com/problems/teemo-attacking/
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:

Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately.
This poisoned status will last 2 seconds until the end of time point 2.
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds.
So you finally need to output 4.


Example 2:

Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned.
This poisoned status will last 2 seconds until the end of time point 2.
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status.
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3.
So you finally need to output 3.

"""
from typing import List
import sys


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        sol = 0
        t = -sys.maxsize
        for i in timeSeries:
            if i - t > duration:
                sol = sol + duration
            else:
                sol = sol + (i - t)
            t = i
        return sol



if __name__ == '__main__':

    timeseries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    duration = 10000
    print ("CASE 1 : Time Series : {}, Duration : {}".format(timeseries, duration))
    sol = Solution().findPoisonedDuration(timeseries, duration)
    print ("Solution : {}".format(sol))

    timeseries = [1, 2, 3, 4, 5]
    duration = 5
    print("CASE 2 : Time Series : {}, Duration : {}".format(timeseries, duration))
    sol = Solution().findPoisonedDuration(timeseries, duration)
    print("Solution : {}".format(sol))

    timeseries = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    duration = 1
    print("CASE 3 : Time Series : {}, Duration : {}".format(timeseries, duration))
    sol = Solution().findPoisonedDuration(timeseries, duration)
    print("Solution : {}".format(sol))

    timeseries = [1, 4]
    duration = 2
    print("CASE 4 : Time Series : {}, Duration : {}".format(timeseries, duration))
    sol = Solution().findPoisonedDuration(timeseries, duration)
    print("Solution : {}".format(sol))