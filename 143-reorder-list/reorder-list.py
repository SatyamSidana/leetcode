# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur=head
        while cur and cur.next:
            pt=cur
            print(pt.val)
            while pt.next and pt.next.next:
                pt=pt.next
            if not pt.next:
                pass
            else:
                t=pt.next
            pt.next=None
            t.next=cur.next
            cur.next=t
            cur=cur.next.next
        return head
        