# leetcode - https://leetcode.com/problems/populating-next-right-pointers-in-each-node
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack=[root]
        while stack:
            cur=stack.pop()
            if cur.left and cur.right:
                cur.left.next=cur.right
                if cur.next:
                    cur.right.next=cur.next.left
                stack.append(cur.right)
                stack.append(cur.left)
        return root
