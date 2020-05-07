# leetcode - https://leetcode.com/problems/perfect-squares/
import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n<=3:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        dp[3]=3
        for i in range(4,n+1):
            dp[i]=i
            for x in range(1,math.ceil(math.sqrt(i))+1):
                temp=x*x
                if temp>i:
                    break
                else:
                    dp[i]=min(dp[i],1+dp[i-temp])
        return dp[n]
