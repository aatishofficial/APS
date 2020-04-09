# leetcode - https://leetcode.com/problems/copy-list-with-random-pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        m={}
        cur=head
        while cur:
            m[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            if cur.next:
                m[cur].next=m[cur.next]
            if cur.random:
                m[cur].random=m[cur.random]
            cur=cur.next
        return m[head]
