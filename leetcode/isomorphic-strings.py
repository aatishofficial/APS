# leetcode - https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True
        m=defaultdict(set)
        for i in range(len(s)):
            m[s[i]].add(t[i])
        for i in m:
            if len(m[i])>1:
                return False
        m=defaultdict(set)
        for i in range(len(t)):
            m[t[i]].add(s[i])
        for i in m:
            if len(m[i])>1:
                return False
        return True
