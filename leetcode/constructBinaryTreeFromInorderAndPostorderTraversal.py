# leetcode - https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            ind=inorder.index(postorder.pop())
            root=TreeNode(inorder[ind])
            root.right=self.buildTree(inorder[ind+1:],postorder)
            root.left=self.buildTree(inorder[:ind],postorder)
            return root
