# leetcode - https://leetcode.com/problems/insertion-sort-list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        helper=ListNode(0)
        cur=head
        pre=helper
        next=None
        while cur:
            next=cur.next
            while pre.next and pre.next.val<cur.val:
                pre=pre.next
            cur.next=pre.next
            pre.next=cur
            pre=helper
            cur=next
        return helper.next
