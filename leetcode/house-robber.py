# leetcode - https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        prev1=prev2=0
        for num in nums:
            tmp=prev1
            prev1=max(num+prev2,prev1)
            prev2=tmp
        return prev1
