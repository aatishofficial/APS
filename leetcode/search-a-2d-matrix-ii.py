# leetcode - https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row=len(matrix)
        col=len(matrix[0])
        i,j=0,col-1
        while 0<=i<row and 0<=j<col:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j] < target:
                i=i+1
            elif matrix[i][j] > target:
                j=j-1
        return False
