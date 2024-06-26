# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sArr=[]
        self.inorder(root)
        return self.sArrBST(0, len(self.sArr)-1)
        
    def inorder(self, root:TreeNode) -> None:
        if not root: return
        self.inorder(root.left)
        self.sArr.append(root)
        self.inorder(root.right)
        
    def sArrBST(self, L:int, R:int) -> TreeNode:
        if L > R: return None
        mid = (L+R) //2
        root = self.sArr[mid]
        root.left = self.sArrBST(L, mid-1)
        root.right = self.sArrBST(mid+1, R)
        return root
