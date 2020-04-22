# leetcode - https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res=float('inf')
        left=0
        val=0
        for i in range(0,len(nums)):
            val+=nums[i]
            while val>=s:
                res=min(res,i+1-left)
                val-=nums[left]
                left+=1
        if res==float('inf'):
            res=0
        return res
