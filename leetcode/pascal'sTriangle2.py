# leetcode - https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[0]*(rowIndex+1)
        res[0]=1
        for i in range(1,rowIndex+1):
            pre=res[:]
            for j in range(1,i+1):
                res[j]=pre[j-1]+pre[j]
        return res
