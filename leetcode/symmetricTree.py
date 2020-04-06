# leetcode - https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.mirror(root,root)
    def mirror(self,t1,t2):
        if t1==None and t2==None:
            return True
        if t1==None or t2==None:
            return False
        return (t1.val==t2.val) and self.mirror(t1.right,t2.left) and self.mirror(t1.left,t2.right)
