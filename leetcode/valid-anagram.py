# leetcode - https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h=collections.defaultdict(int)
        for i in range(len(s)):
            h[s[i]]+=1
            h[t[i]]-=1
        for val in h:
            if h[val]!=0:
                return False
        return True
