# leetcode - https://leetcode.com/problems/longest-palindromic-substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength=1
        start=0
        table=[[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            table[i][i]=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                table[i][i+1]=1
                start=i
                maxlength=2
        for k in range(3,len(s)+1):
            for i in range(len(s)-k+1):
                j=i+k-1
                if table[i+1][j-1]==1 and s[i]==s[j]:
                    table[i][j]=1
                    if k>maxlength:
                        start=i
                        maxlength=k
        return s[start:start+maxlength]
