# leetcode - https://leetcode.com/problems/linked-list-cycle-ii
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return None
        slow=fast=entry=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=entry:
                    slow=slow.next
                    entry=entry.next
                return entry
        return None
