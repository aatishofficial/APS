# leetcode - https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        l=[]
        for i in range(32):
            t=n & 1
            l.append(t)
            n=n>>1
        res=0
        for i in range(len(l)):
            res=res<<1
            res=res | l[i]
        return res
