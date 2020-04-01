# leetcode - https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<h:
            mid=l+(h-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                h=mid-1
            else:
                l=mid+1
        return l+1 if target>nums[l] else l
