# leetcode - https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            t=sum([int(i) for i in str(num)])
            num=t
        return num
