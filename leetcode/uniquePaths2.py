# leetcode - https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0]*m for _ in range(n)]
        dp[0][0]=1-obstacleGrid[0][0]
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]*(1-obstacleGrid[i][0])
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]*(1-obstacleGrid[0][i])
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=(dp[i][j-1]+dp[i-1][j])*(1-obstacleGrid[i][j])
        return dp[-1][-1]
