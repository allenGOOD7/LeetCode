"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        origin = root
        while root:
            cur = temp = Node(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = root.left
                if root.right:
                    cur.next = root.right
                    cur = root.right
                root = root.next
            root = temp.next
        return origin