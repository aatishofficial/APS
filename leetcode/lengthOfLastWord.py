# leetcode - https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==0:
            return 0
        res=0
        pointer=len(s)-1
        while pointer>=0 and s[pointer]==' ':
            pointer-=1
        if pointer==-1:
            return 0
        for i in range(pointer,-1,-1):
            if s[i]!=' ':
                res+=1
            else:
                break
        return res
