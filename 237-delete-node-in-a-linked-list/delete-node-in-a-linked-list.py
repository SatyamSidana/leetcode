# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        cur=node
        while cur and cur.next :
            a=cur.next.val
            cur.next.val=cur.val
            cur.val=a
            ptr=cur
            cur=cur.next
        ptr.next=None      
        