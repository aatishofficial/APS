# leetcode - https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        rob1=self.help(nums[1:])
        rob2=self.help(nums[0:len(nums)-1])
        return max(rob1,rob2)
        
    def help(self,nums):
        if len(nums)==0:
            return 0
        pre=0
        cur=nums[0]
        for i in range(1,len(nums)):
            t=max(pre+nums[i],cur)
            pre=cur
            cur=t
        return cur
