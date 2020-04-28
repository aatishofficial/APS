# leetcode - https://leetcode.com/problems/single-number-iii/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        h=collections.defaultdict(int)
        res=[]
        for n in nums:
            h[n]+=1
        for n in h:
            if h[n]==1:
                res.append(n)
        return res
