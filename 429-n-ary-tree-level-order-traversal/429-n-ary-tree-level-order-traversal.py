"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = [root]
        
        while queue:
            res.append([])
            for i in range(len(queue)):
                node = queue.pop(0)
                res[-1].append(node.val)
                
                for child in node.children:
                    queue.append(child)
        return res