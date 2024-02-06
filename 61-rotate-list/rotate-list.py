# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        c=1
        if not cur:
            return head
        while cur and cur.next:
            c+=1
            cur=cur.next
        m=k%c
        pt=cur=head
        while m:
            cur=cur.next
            m-=1
        while cur and  cur.next:
            pt=pt.next
            cur=cur.next
        cur.next=head
        head=pt.next
        pt.next=None
        return head
            