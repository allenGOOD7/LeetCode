# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def traversal(root, level):
            if len(ans) < level:
                ans.append([root.val])
            else:
                ans[level-1].append(root.val)
                
            if root.left is not None:
                traversal(root.left, level+1)
            if root.right is not None:
                traversal(root.right, level+1)
        if root:
            traversal(root, 1)
        return ans