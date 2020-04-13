# leetcode - https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, s: str) -> int:
        dic={chr(i+64):i for i in range(1,27)}
        res=0
        s=s[::-1]
        for i,c in enumerate(s):
            res+=dic[c]*(26**i)
        return res
