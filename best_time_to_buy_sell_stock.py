'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = None
        profit = 0
        for i in range(1, len(prices)):
            curr = prices[i]
            if curr - buy > profit:
                sell = curr
                profit = sell - buy
            elif curr < buy:
                buy = curr
                sell = None
        return profit    