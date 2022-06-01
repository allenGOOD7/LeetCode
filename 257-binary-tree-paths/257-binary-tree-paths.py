# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        
        def dfs(node, path):
            path += '->' + str(node.val)
            if not node.left and not node.right:
                result.append(path)
            
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
                
        path = str(root.val)
        if not root.left and not root.right:
            result.append(path)
        else:
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
            
        return result
            