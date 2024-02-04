# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        if not cur or not cur.next:
            return head
        if not cur.next.next:
            if cur.val==cur.next.val:
                return cur.next.next
        while cur and cur.next :
            if cur==head and cur.val==cur.next.val:
                d=cur.next
                while d and cur.val==d.val:
                    d=d.next
                head=d
                cur=head
            else:
                if cur.next.next and  cur.next.val==cur.next.next.val:
                    d=cur.next.next
                    while d and cur.next.val==d.val:
                        d=d.next
                    cur.next=d
                else:
                    cur=cur.next
        return head
        