#leetcode https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map={}
        max_length=start=0
        for i in range(len(s)):
            if s[i] in map and start<=map[s[i]]:
                start=map[s[i]]+1
            else:
                max_length=max(max_length,i-start+1)
            map[s[i]]=i
        return max_length
