# leetcode - https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        n=1
        newH=tail=head
        while tail.next:
            tail=tail.next
            n+=1
        tail.next=head
        k=k%n
        if k:
            for i in range(n-k):
                tail=tail.next
        newH=tail.next
        tail.next=None
        return newH
