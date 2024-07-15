# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, d: List[List[int]]) -> Optional[TreeNode]:
        a={}
        for i in d:
            if i[0] not in a:
                a[i[0]]=TreeNode(i[0],None,None)
            if i[1] not in a:
                a[i[1]]=TreeNode(i[1],None,None)
        for i in d:
            if i[2]==1:
                a[i[0]].left=a[i[1]]
            else:
                a[i[0]].right=a[i[1]]
        for i in d:
            a.pop(i[1])
        for i in a:
            return a[i]