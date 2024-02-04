# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        if not head:
            return head
        while cur and cur.next:
            if cur.val==cur.next.val:
                d=cur.next
                while d and d.val==cur.val :
                    d=d.next
                cur.next=d
                cur=d
            else:
                cur=cur.next
        return head