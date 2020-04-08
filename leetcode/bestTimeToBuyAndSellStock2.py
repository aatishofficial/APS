# leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=(prices[i+1]-prices[i])
        return profit
