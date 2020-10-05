"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""

#!/usr/bin/env python
# -*- coding: utf-8
__author__ = "Parkash Sharma"

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = 0
        max_index = 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i
                max_index = i
            if prices[i] > prices[max_index]:
                max_index = i
                profit = prices[max_index] - prices[min_index]
                if profit > max_profit:
                    max_profit = profit
        return max_profit


if  __name__ == '__main__':
    print ("Running Best Time to Buy and Sell Stock Program")
    prices = [7, 1, 5, 3, 6, 4]
    print ("Case 1 : {}".format(prices))
    print (Solution().maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print("Case 2 : {}".format(prices))
    print(Solution().maxProfit(prices))