# leetcode - https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        s='1'
        for i in range(n-1):
            temp1,temp,count=s[0],'',0
            for l in s:
                if temp1==l:
                    count+=1
                else:
                    temp+=str(count)+temp1
                    temp1=l
                    count=1
            temp+=str(count)+temp1
            s=temp
        return s
