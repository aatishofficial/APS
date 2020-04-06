# leetcode - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.help(nums,0,len(nums)-1)
    def help(self,nums,left,right):
        if left>right:
            return None
        mid=left+(right-left)//2
        node=TreeNode(nums[mid])
        node.left=self.help(nums,left,mid-1)
        node.right=self.help(nums,mid+1,right)
        return node
