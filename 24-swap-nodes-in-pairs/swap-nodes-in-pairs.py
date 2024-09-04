# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=cur=ListNode()
        ptr=head
        a=[]
        k=2
        while ptr:
            a.append(ptr)
            ptr=ptr.next
            if len(a)==k:
                while a:
                    b=a.pop()
                    cur.next=b
                    cur=cur.next
                    cur.next=None
        while a:
            b=a.pop(0)
            cur.next=b
            cur=cur.next
            cur.next=None
        return dummy.next
        