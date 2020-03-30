# leetcode - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        short=min(strs,key=len)
        for i,ch in enumerate(short):
            for other in strs:
                if other[i]!=ch:
                    return short[:i]
        return short
