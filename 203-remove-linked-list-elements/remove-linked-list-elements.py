# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], v: int) -> Optional[ListNode]:
        cur=head
        while cur :
            if cur==head and cur.val==v:
                head=head.next
                cur=head
            else:
                d=cur.next
                while d and d.val==v:
                    d=d.next
                cur.next=d
                cur=cur.next
        return head


        