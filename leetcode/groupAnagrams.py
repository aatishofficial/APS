# leetcode - https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            key=tuple(sorted(word))
            d[key]=d.get(key,[])+[word]
        return list(d.values())
