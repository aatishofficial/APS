# leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t_i10,t_i11,t_i20,t_i21=0,float('-inf'),0,float('-inf')
        for price in prices:
                t_i20=max(t_i20,t_i21+price)
                t_i21=max(t_i21,t_i10-price)
                t_i10=max(t_i10,t_i11+price)
                t_i11=max(t_i11,-price)
        return t_i20
