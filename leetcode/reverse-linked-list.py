# leetcode - https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur=head
        next=prev=None
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev