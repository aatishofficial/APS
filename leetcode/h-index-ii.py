# leetcode - https://leetcode.com/problems/h-index-ii/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i<j for i,j in enumerate(sorted(citations,reverse=True)))
