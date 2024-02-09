# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        d=ListNode()
        d.next=head
        cur=d
        a=[]
        if not head or l==r:
            return head
        for _ in range(l - 1):
            cur=cur.next
        ptr=cur.next
        for _ in range(r - l + 1):
            a.append(ptr)
            ptr=ptr.next
        while a:
            n=a.pop()
            cur.next=n
            cur=cur.next
        cur.next=ptr
        return d.next


        


        