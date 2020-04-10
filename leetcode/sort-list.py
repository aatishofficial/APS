# leetcode - https://leetcode.com/problems/sort-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self,left,right):
        dummy=ListNode(0)
        pre=dummy
        while left and right:
            if left.val<=right.val:
                pre.next=left
                left=left.next
            else:
                pre.next=right
                right=right.next
            pre=pre.next
        if right:
            pre.next=right
        if left:
            pre.next=left
        return dummy.next
    def sortList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        slow,fast,temp=head,head,None
        while fast and fast.next:
            temp=slow
            slow=slow.next
            fast=fast.next.next
        temp.next=None
        left=self.sortList(head)
        right=self.sortList(slow)
        return self.merge(left,right)
