# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        dummy=ListNode()
        cur=dummy
        while l1 and l2:
            m=l1.val+l2.val+c
            if m>9:
                t=ListNode(m-10)
                cur.next=t
                c=1
            else:
                t=ListNode(m)
                cur.next=t
                c=0
            cur,l1,l2=cur.next,l1.next,l2.next
        if l1:
            while l1:
                m=l1.val+c
                if m>9:
                    t=ListNode(m-10)
                    cur.next=t
                    c=1
                else:
                    t=ListNode(m)
                    cur.next=t
                    c=0
                cur,l1=cur.next,l1.next
        if l2:
            while l2:
                m=l2.val+c
                if m>9:
                    t=ListNode(m-10)
                    cur.next=t
                    c=1
                else:
                    t=ListNode(m)
                    cur.next=t
                    c=0
                cur,l2=cur.next,l2.next
        if c:
            t=ListNode(1)
            cur.next=t

        return dummy.next


        