# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        c=0
        if not head.next:
            return None
        if not head.next.next:
            cur.next=None
            return head
        pt=head
        pt=pt.next
        cur=cur.next.next
        d=head
        while cur and cur.next:
            d=d.next
            pt=pt.next
            cur=cur.next.next
        d.next=d.next.next
        '''c=c//2
        m=0
        cur=head
        while m<c-1:
            cur=cur.next
            m+=1
        cur.next=cur.next.next'''
        return head
        