# leetcode - https://leetcode.com/problems/maximum-product-subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max_pro=nums[0]
        cur_min_pro=nums[0]
        pre_max_pro=nums[0]
        pre_min_pro=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            cur_max_pro=max(pre_max_pro*nums[i],pre_min_pro*nums[i],nums[i])
            cur_min_pro=min(pre_max_pro*nums[i],pre_min_pro*nums[i],nums[i])
            ans=max(ans,cur_max_pro)
            pre_max_pro=cur_max_pro
            pre_min_pro=cur_min_pro
        return ans
