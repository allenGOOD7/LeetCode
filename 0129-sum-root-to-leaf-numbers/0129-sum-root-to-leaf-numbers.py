# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0)
            
        return self.res
        
        
    def dfs(self, root, path):       
        if not root:
            return 0
        if not root.left and not root.right:
            self.res += (path * 10 + root.val)
        self.dfs(root.left, path * 10 + root.val)
        self.dfs(root.right, path * 10 + root.val)
        