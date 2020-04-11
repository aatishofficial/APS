# leetcode - https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in ['+','-','*','/']:
                stack.append(int(tokens[i]))
            else:
                op2=stack.pop()
                op1=stack.pop()
                res=0
                if tokens[i]=='+':
                    res=op1+op2
                elif tokens[i]=='-':
                    res=op1-op2
                elif tokens[i]=='*':
                    res=op1*op2
                else:
                    res=op1//op2
                    if op1*op2<0 and op1%op2!=0:
                        res+=1
                stack.append(res)
        return stack.pop()
