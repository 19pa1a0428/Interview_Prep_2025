"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

##Brute force --> will lead to time limit exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        n = len(prices)

        for i in range(n):
            for j in range(i+1,n):
                if prices[j]>prices[i]:
                    maxx = max(prices[j]-prices[i], maxx)
        return maxx


        

##Optimal approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        maxx = 0
        for i in range(len(prices)):
            minn = min(prices[i], minn)
            maxx = max(maxx, prices[i] - minn)
        return maxx
