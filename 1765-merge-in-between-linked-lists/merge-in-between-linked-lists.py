# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        d=ListNode()
        d.next=list1
        prev=cur=d
        for i in range (a):
            cur=cur.next
        prev=cur.next
        cur.next=list2
        cur=cur.next
        while cur and cur.next:
            cur=cur.next
        print(cur.val)
        
        for i in range (b-a+1):
            prev=prev.next
        cur.next=prev
        return d.next


        