# leetcode - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        pre,cur=dummy,dummy.next
        while cur:
            if cur.next and cur.val ==cur.next.val:
                temp=cur.val
                while cur and cur.val == temp:
                    cur=cur.next
                pre.next=cur
            else:
                pre,cur=cur,cur.next
        return dummy.next
