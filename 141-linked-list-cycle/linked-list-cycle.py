# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a={}
        cur=head
        while cur:
            if a.get(cur):
                return True
            else:
                a[cur]=1
            cur=cur.next
        return False
        