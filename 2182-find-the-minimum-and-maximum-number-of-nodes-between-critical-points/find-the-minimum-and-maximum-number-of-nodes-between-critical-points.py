# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur=head.next.next
        prev=head.next
        a=[]
        m=head.val
        if not cur:
            return [-1,-1]
        c=2
        mi=10**5
        while cur :
            if m<prev.val>cur.val or cur.val>prev.val<m:
                a.append(c)
            if len(a)>1:
                mi=min(mi,a[-1]-a[-2])
            c+=1
            m=prev.val
            cur=cur.next
            prev=prev.next
        if len(a)<2:
            return [-1,-1]
        return [mi,a[-1]-a[0]]
        

        