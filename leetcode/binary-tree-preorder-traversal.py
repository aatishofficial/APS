# leetcode - https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        self.dfs(root,res)
        return res
    def dfs(self,root,res):
        if root:
            res.append(root.val)
            self.dfs(root.left,res)
            self.dfs(root.right,res)
