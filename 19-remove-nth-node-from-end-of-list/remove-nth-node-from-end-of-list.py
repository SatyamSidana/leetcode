# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        d=cur
        
        for i in range (n):
            d=d.next
        if not d:
            return head.next
        while d.next:
            cur=cur.next
            d=d.next
            
        cur.next=cur.next.next
        return head

        