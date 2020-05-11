# leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t_ik0_pre,t_ik0,t_ik1=0,0,float('-inf')
        for price in prices:
            t_ik0_old=t_ik0
            t_ik0=max(t_ik0,t_ik1+price)
            t_ik1=max(t_ik1,t_ik0_pre-price)
            t_ik0_pre=t_ik0_old
        return t_ik0
