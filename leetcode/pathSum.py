# leetcode - https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue=collections.deque([(root,root.val)])
        while queue:
            cur,val=queue.popleft()
            if not cur.left and not cur.right:
                if val==sum:
                    return True
            if cur.left:
                queue.append((cur.left,val+cur.left.val))
            if cur.right:
                queue.append((cur.right,val+cur.right.val))
        return False
