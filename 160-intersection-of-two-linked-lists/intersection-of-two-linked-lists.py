# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a={}
        cur=headA
        pt=headB
        while cur:
            a[cur]=1
            cur=cur.next
        while pt:
            if a.get(pt) :
                return pt
            else:
                pt=pt.next
        t=None
        return t
        