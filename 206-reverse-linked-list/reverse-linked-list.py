# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode()
        d=d.next
        cur=head
        while cur:
            t=ListNode(cur.val)
            t.next=d
            d=t
            cur=cur.next
        return d

        