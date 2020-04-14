# leetcode - https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        slow=fast=n
        first=True
        while first or slow!=fast:
            first=False
            slow=sum([int(i)**2 for i in str(slow)])
            fast=sum([int(i)**2 for i in str(fast)])
            fast=sum([int(i)**2 for i in str(fast)])
        return slow==1
