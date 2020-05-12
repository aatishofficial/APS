# leetcode - https://leetcode.com/problems/house-robber-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.help(root,{})
    def help(self,root,m):
        if not root:
            return 0
        if root in m:
            return m[root]
        val=0
        if root.left:
            val+=self.help(root.left.left,m)+self.help(root.left.right,m)
        if root.right:
            val+=self.help(root.right.left,m)+self.help(root.right.right,m)
        val=max(val+root.val,self.help(root.left,m)+self.help(root.right,m))
        m[root]=val
        return val
