# leetcode - https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
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
        queue=collections.deque([root])
        nextLevel=collections.deque([])
        while queue:
            node=queue.popleft()
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if queue:
                node.next=queue[0]
            if not queue:
                queue,nextLevel=nextLevel,queue
        return root
