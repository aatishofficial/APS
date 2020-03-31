# leetcode - https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive=(dividend < 0) is (divisor <0 )
        a,b=abs(dividend),abs(divisor)
        res=0
        while a>=b:
            temp,i=b,1
            while a>=temp:
                a-=temp
                res+=i
                i<<=1
                temp<<=1
        if not positive:
            res=-res
        return min(max(-2147483648,res),2147483647)
