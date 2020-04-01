# leetcode - https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        cur=m=nums[0]
        for num in nums[1:]:
            cur=max(num,cur+num)
            m=max(cur,m)
        return m
