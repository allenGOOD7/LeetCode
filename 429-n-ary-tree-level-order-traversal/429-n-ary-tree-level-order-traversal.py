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
        res.append([root.val])
        
        def dfs(root, level):
            if not root:
                return 
            for node in root:
                if len(res) <= level:
                    res.append([node.val])
                else:
                    # print(res, node.val, level)
                    res[level].append(node.val)
                dfs(node.children, level + 1)
        
        if root.children:
            dfs(root.children, 1)
            
        return res
