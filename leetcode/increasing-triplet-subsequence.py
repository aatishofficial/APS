# leetcode - https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        res=False
        if len(nums)>0:
            first=nums[0]
            second=float('inf')
            for i in range(1,len(nums)):
                if res:
                    break
                if nums[i]>second:
                    res=True
                elif nums[i]>first and nums[i]<second:
                    second=nums[i]
                elif nums[i]<first:
                    first=nums[i]
        return res
