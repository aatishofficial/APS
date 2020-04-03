# leetcode -  https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start,index,end=0,0,len(nums)-1
        while index<=end and start < end:
            if nums[index]==0:
                nums[index]=nums[start]
                nums[start]=0
                start+=1
                index+=1
            elif nums[index]==2:
                nums[index]=nums[end]
                nums[end]=2
                end-=1
            else:
                index+=1
