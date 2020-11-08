"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.



Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.

"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        print (asteroids)
        start = 0
        end = len(asteroids)-2
        while start <= end and len(asteroids) > 1:
            if asteroids[end] > 0 and asteroids[end+1] < 0:
                if abs(asteroids[end]) < abs(asteroids[end+1]):
                    asteroids[end] = asteroids[end+1]
                    del asteroids[end+1]
                elif abs(asteroids[end]) == abs(asteroids[end+1]):
                    del asteroids[end+1]
                    del asteroids[end]
                    end = end if end + 1 <= len(asteroids) else end - 1
                else:
                    del asteroids[end+1]
                    end = end + 1 if end + 2 <= len(asteroids) else end
            end = end - 1
        return asteroids


if __name__ == '__main__':
    asteroids = [5, 10, -5]
    print ("Case 1 : Asteriods : {}".format(asteroids))
    sol = Solution().asteroidCollision(asteroids)
    print ("Solution : {}".format(sol))

    asteroids = [8,-8]
    print("Case 2 : Asteriods : {}".format(asteroids))
    sol = Solution().asteroidCollision(asteroids)
    print("Solution : {}".format(sol))

    asteroids = [10,2,-5]
    print("Case 3 : Asteriods : {}".format(asteroids))
    sol = Solution().asteroidCollision(asteroids)
    print("Solution : {}".format(sol))

    asteroids = [-2,-2,1,-1]
    print("Case 4 : Asteriods : {}".format(asteroids))
    sol = Solution().asteroidCollision(asteroids)
    print("Solution : {}".format(sol))

    asteroids = [1,1,-1,-2]
    print("Case 5 : Asteriods : {}".format(asteroids))
    sol = Solution().asteroidCollision(asteroids)
    print("Solution : {}".format(sol))