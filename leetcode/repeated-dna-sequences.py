# leetcode - https://leetcode.com/problems/repeated-dna-sequences/
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic=collections.defaultdict(int)
        for i in range(len(s)):
            dic[s[i:i+10]]+=1
        return [key for key in dic.keys() if dic[key]>1]
