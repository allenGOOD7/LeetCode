# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        hash_set = set()
        
        def dfs(root):
            if not root:
                return False
            if k - root.val in hash_set:
                return True
            else:
                hash_set.add(root.val)
            
            # if root.right:
            #     dfs(root.right)
            # if root.left:
            #     dfs(root.left)
            return dfs(root.right) or dfs(root.left)
        
        # dfs(root)
        
        # for element in hash_set:
        #     if k - element in hash_set:
        #         return True
        
        return dfs(root)