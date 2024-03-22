# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p=ListNode(None)
        ptr=head
        while ptr:
            t=ListNode(ptr.val)
            t.next=p
            p=t
            ptr=ptr.next
        cur=p
        ptr=head
        while ptr:
            print(cur.val)
            if ptr.val==cur.val:
                ptr=ptr.next
                cur=cur.next
            else:
                return False
        return True


        