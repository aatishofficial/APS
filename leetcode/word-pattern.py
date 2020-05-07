# leetcode - https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))
