# leetcode - https://leetcode.com/problems/fraction-to-recurring-decimal
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        res=""
        if (numerator<0) ^ (denominator<0):
            res+='-'
        n=abs(numerator)
        d=abs(denominator)
        res+=str(n//d)
        if n%d==0:
            return res
        res+='.'
        h={}
        r=n%d
        while r:
            if r in h:
                res=res[:h[r]]+'('+res[h[r]:]+')'
                break
            h[r]=len(res)
            r*=10
            res+=str(r//d)
            r%=d
        return res
