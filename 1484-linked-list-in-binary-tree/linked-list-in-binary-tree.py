# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        a=[]
        b=[]
        c=0
        r=head
        while r:
            c+=1
            r=r.next
        def check(a,pt):
            i=0
            ptr=pt
            while i <len(a)-c+1:
                if a[i]==ptr.val:
                    j=i
                    i+=1
                    while j<len(a) and ptr and a[j]==ptr.val:
                        j+=1
                        ptr=ptr.next    
                    if ptr==None:
                        return True
                    else:
                        ptr=pt
                else:
                    i+=1
            return False
        def preorder(cur):
            if cur!=None:
                a.append(cur.val)
                preorder(cur.left)
                preorder(cur.right)
                if cur.left==None and cur.right==None:
                    if check(list(a),head):
                        b.append(1)
                a.pop()
        preorder(root)
        if len(b)>0:
            return True
        return False
                    
        