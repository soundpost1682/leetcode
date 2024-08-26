"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        answer =[]
        def deep(root):
            for i in root.children:
                deep(i)
            answer.append(root.val)
        
        deep(root)
        return answer
