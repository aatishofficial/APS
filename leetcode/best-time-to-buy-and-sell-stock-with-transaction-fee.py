# leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        t_ik0,t_ik1=0,float('-inf')
        for price in prices:
            t_ik0_old=t_ik0
            t_ik0=max(t_ik0,t_ik1+price-fee)
            t_ik1=max(t_ik1,t_ik0_old-price)
        return int(t_ik0)
