# leetcode - https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return 0
        if digits[len(digits)-1]<9:
            digits[len(digits)-1]+=1
            return digits
        carry,digits[len(digits)-1]=divmod(digits[len(digits)-1]+1,10)
        i=len(digits)-2
        while i>=0 and carry:
            carry,digits[i]=divmod(digits[i]+1,10)
            i-=1
        if carry:
            digits=[carry]+digits
        return digits
