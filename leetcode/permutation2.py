# leetcode - https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        used=[False]*len(nums)
        self.back(res,[],used,nums)
        return res
    def back(self,res,temp,used,nums):
        if len(temp)==len(nums):
            res.append(temp)
        for i in range(len(nums)):
            if used[i] or i>0 and nums[i]==nums[i-1] and used[i-1]==False:
                continue
            used[i]=True
            self.back(res,temp+[nums[i]],used,nums)
            used[i]=False
