# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=cur=head
        c=0
        while ptr and ptr.next: 
            ptr=ptr.next.next
            cur=cur.next
        return cur
        