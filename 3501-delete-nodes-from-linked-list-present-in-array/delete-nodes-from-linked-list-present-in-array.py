# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        a={}
        for i in nums:
            a[i]=1
        dummy=cur=ListNode()
        ptr=head
        while ptr:
            while ptr and ptr.val in a:
                ptr=ptr.next
            if ptr:
                cur.next=ptr
                cur=cur.next
                ptr=ptr.next
        cur.next=None
        return dummy.next