# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        if not head.next:
            return head
        ohead=head
        ehead=e=head.next
        while e and e.next:
            ohead.next=ohead.next.next
            e.next=e.next.next
            ohead=ohead.next
            e=e.next
        ohead.next=ehead
        return head



        