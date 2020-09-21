"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
"""
#!/usr/bin/env python
# -*- coding: utf-8
__author__ = "Parkash Sharma"

from typing import List


class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger_count = {}
        for i in trips:
            cap, start, end = i
            for k in range(start + 1, end + 1):
                passenger_count[k] = passenger_count.get(k, 0) + cap
                if passenger_count[k] > capacity:
                    return False

        return True


if __name__ == '__main__':
    print ("Running Car Pooling Program")
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    print("Case 1 : Trips : {}, Capacity : {}".format(trips, capacity))
    print (Solution().carPooling(trips, capacity))

    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5
    print("Case 2 : Trips : {}, Capacity : {}".format(trips, capacity))
    print (Solution().carPooling(trips, capacity))

    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3
    print("Case 3 : Trips : {}, Capacity : {}".format(trips, capacity))
    print (Solution().carPooling(trips, capacity))

    trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
    capacity = 11
    print("Case 4 : Trips : {}, Capacity : {}".format(trips, capacity))
    print (Solution().carPooling(trips, capacity))