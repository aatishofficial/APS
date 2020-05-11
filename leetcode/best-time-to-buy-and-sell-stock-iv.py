# leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k>=(len(prices)>>1):
            t_ik0,t_ik1=0,float('-inf')
            for price in prices:
                t_ik0_old=t_ik0
                t_ik0=max(t_ik0,t_ik1+price)
                t_ik1=max(t_ik1,t_ik0_old-price)
            return t_ik0
        t_ik0=[0]*(k+1)
        t_ik1=[float('-inf')]*(k+1)
        for price in prices:
            for j in range(k,0,-1):
                t_ik0[j]=max(t_ik0[j],t_ik1[j]+price)
                t_ik1[j]=max(t_ik1[j],t_ik0[j-1]-price)
        return t_ik0[k]
