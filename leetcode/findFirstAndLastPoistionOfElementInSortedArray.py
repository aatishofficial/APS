# leetcode - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def extreme(self,nums,target,left):
        l=0
        h=len(nums)
        while l<h:
            mid=(l+h)//2
            if nums[mid] > target or (left and target == nums[mid]):
                h=mid
            else:
                l=mid+1
        return l
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx=self.extreme(nums,target,True)
        if left_idx == len(nums) or nums[left_idx] !=target:
            return [-1,-1]
        return [left_idx,self.extreme(nums,target,False)-1]
