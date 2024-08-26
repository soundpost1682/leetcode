"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def tmp(root):
            if root:
                for i in root.children:
                    tmp(i)
                tmp2.append(root.val)
        tmp2 =[]
        tmp(root)
        return tmp2
