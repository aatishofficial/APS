# leetcode - https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        data=preorder.split(',')
        count=1
        for d in data:
            if count==0:
                return False
            if d=='#':
                count-=1
            else:
                count+=1
        return count==0
