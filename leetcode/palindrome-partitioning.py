# leetcode - https://leetcode.com/problems/palindrome-partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.dfs(s,[],res)
        return res
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
        for i in range(1,len(s)+1):
            if self.ispar(s[:i]):
                self.dfs(s[i:],path+[s[:i]],res)
    def ispar(self,s):
        return s==s[::-1]
