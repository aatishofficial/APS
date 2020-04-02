# leetcode - https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l,r=1,x
        ans=1
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                l=mid+1
                ans=mid
            else:
                r=mid-1
        return ans
