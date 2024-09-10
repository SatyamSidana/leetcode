# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        ptr=head
        while ptr and ptr.next:
            temp=ListNode(gcd(ptr.val,ptr.next.val))
            temp.next=ptr.next
            ptr.next=temp
            ptr=ptr.next.next
        return head

        
