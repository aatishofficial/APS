# leetcode - https://leetcode.com/problems/same-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not q or not p:
                return False
            if p.val!=q.val:
                return False
            return True
        deq=deque([(p,q),])
        while deq:
            p,q=deq.popleft()
            if not check(p,q):
                return False
            if p:
                deq.append((p.left,q.left))
                deq.append((p.right,q.right))
        return True
