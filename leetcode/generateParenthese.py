# leetcode - https://leetcode.com/problems/generate-parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def back(s='',left=0,right=0):
            if len(s)==2*n:
                ans.append(s)
                return
            if left<n:
                back(s+'(',left+1,right)
            if right<left:
                back(s+')',left,right+1)
        back()
        return ans
