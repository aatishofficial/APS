# leetcode - https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        x=len(nums1)
        y=len(nums2)
        l,r=0,x
        while l<=r:
            partitionX=(l+r)//2
            partitionY=(x+y+1)//2 - partitionX
            maxleftX=nums1[partitionX-1] if partitionX!=0 else float('-inf')
            minrightX=nums1[partitionX] if partitionX!=x else float('inf')
            maxleftY=nums2[partitionY-1] if partitionY!=0 else float('-inf')
            minrightY=nums2[partitionY] if partitionY!=y else float('inf')
            if maxleftX<=minrightY and maxleftY<=minrightX:
                if (x+y)%2 == 0:
                    return (max(maxleftX,maxleftY) + min(minrightX,minrightY)) / 2
                else:
                    return max(maxleftX,maxleftY)
            elif maxleftX > minrightY:
                r=partitionX-1
            else:
                l=partitionX+1
