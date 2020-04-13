# leetcode - https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        cap=[chr(i) for i in range(ord('A'),ord('Z')+1)]
        res=[]
        while n>0:
            res.append(cap[(n-1)%26])
            n=(n-1)//26
        res.reverse()
        return ''.join(res)
