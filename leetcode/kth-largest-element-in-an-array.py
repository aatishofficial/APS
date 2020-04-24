# leetcode - https://leetcode.com/problems/kth-largest-element-in-an-array/
from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l,r):
            pivotIndex=randint(l,r)
            pivot=nums[pivotIndex]
            nums[pivotIndex],nums[r]=nums[r],nums[pivotIndex]
            i=l-1
            for j in range(l,r):
                if nums[j]<pivot:
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]
            nums[i+1],nums[r]=nums[r],nums[i+1]
            return i+1
        l,r,k=0,len(nums)-1,len(nums)-k
        while True:
            pos=partition(l,r)
            if k>pos:
                l=pos+1
            elif k<pos:
                r=pos-1
            else:
                return nums[pos]
