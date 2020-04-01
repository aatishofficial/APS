# leetcode - https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=set()
        self.per(res,visited,[],nums)
        return res
    def per(self,res,visited,subset,nums):
        if len(subset)==len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.per(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
