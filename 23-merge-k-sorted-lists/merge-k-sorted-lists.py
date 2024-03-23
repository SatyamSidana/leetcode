# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        for i in lists:
            ptr=i
            while ptr:
                a.append(ptr.val)
                ptr=ptr.next
        heapq.heapify(a)
        p=ListNode(0)
        cur=p
        for i in range (len(a)):
            b=heapq.heappop(a)
            t=ListNode(b)
            cur.next=t
            cur=cur.next
        return p.next
        