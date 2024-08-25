# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer =[]
        def spot(root):
            if root:
                spot(root.left)
                spot(root.right)
                answer.append(root.val)
        spot(root)
        return answer
        
