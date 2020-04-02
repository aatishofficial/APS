# leetcode - https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[j for sub in matrix for j in sub]
        l=0
        r=len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==target:
                return True
            elif arr[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
