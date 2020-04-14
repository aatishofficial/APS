# leetcode - https://leetcode.com/problems/bitwise-and-of-numbers-range/
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m<n:
            n=n&(n-1)
        return n
