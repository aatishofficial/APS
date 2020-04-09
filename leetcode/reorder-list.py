# leetcode - https://leetcode.com/problems/reorder-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self,l1,l2):
        while l1:
            l1_next=l1.next
            l2_next=l2.next
            l1.next=l2
            if l1_next==None:
                break
            l2.next=l1_next
            l1=l1_next
            l2=l2_next
    def reverse(self,head):
        pre=None
        cur=head
        while cur:
            next_node=cur.next
            cur.next=pre
            pre=cur
            cur=next_node
        return pre
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return
        pre,slow,fast=None,head,head
        l1=head
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        pre.next=None
        l2=self.reverse(slow)
        self.merge(l1,l2)
