# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=cur=head
        c=0
        while ptr: 
            c+=1
            ptr=ptr.next
        c=c//2
        
        for i in range (c):
            cur=cur.next
        return cur
        