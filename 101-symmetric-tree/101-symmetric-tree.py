# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        root1 = root.left
        root2 = root.right
        def fun(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            
            if root1.val == root2.val:
                x = fun(root1.right, root2.left)
                y = fun(root1.left, root2.right)
                
                if x == True and y == True:
                    return True
                return False
        return fun(root1, root2)
        