# leetcode - https://leetcode.com/problems/sum-root-to-leaf-numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack,res=[(root,root.val)],0
        while stack:
            node,val=stack.pop()
            if node:
                if not node.left and not node.right:
                    res+=val
                if node.right:
                    stack.append((node.right,val*10+node.right.val))
                if node.left:
                    stack.append((node.left,val*10+node.left.val))
        return res
