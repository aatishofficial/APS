# leetcode - https://leetcode.com/problems/multiply-strings/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product=[0]*(len(num1)+len(num2))
        position=len(product)-1
        for n1 in num1[::-1]:
            tempPos=position
            for n2 in num2[::-1]:
                product[tempPos]+=int(n1)*int(n2)
                product[tempPos-1]+=product[tempPos]//10
                product[tempPos]%=10
                tempPos-=1
            position-=1
        pointer=0
        while pointer < len(product)-1 and product[pointer]==0:
            pointer+=1
        return ''.join(map(str,product[pointer:]))
