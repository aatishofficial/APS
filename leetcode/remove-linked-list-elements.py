# leetcode - https://leetcode.com/problems/remove-linked-list-elements
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        cur=head
        while cur:
            t=cur.next
            if cur.val==val:
                prev.next=t
                cur.next=None
            else:
                prev=cur
            cur=t
        return dummy.next
