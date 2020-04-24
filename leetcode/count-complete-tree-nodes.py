# leetcode - https://leetcode.com/problems/count-complete-tree-nodes/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        hleft=hright=0
        pleft=pright=root
        while pleft:
            hleft+=1
            pleft=pleft.left
        while pright:
            hright+=1
            pright=pright.right
        if hleft==hright:
            return 2**hleft - 1
        return self.countNodes(root.left)+self.countNodes(root.right)+1
