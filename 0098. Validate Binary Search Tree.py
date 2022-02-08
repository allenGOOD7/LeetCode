import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def solve(root, minValue, maxValue):
            if not root:
                return True
            if minValue < root.val < maxValue:
                return solve(root.left, minValue, root.val) and solve(root.right, root.val, maxValue)
            else:
                return False
        
        return solve(root, -sys.maxsize, sys.maxsize)

# testCase 
tree = TreeNode(2,TreeNode(1),TreeNode(3))
print(Solution().isValidBST(tree))
tree = TreeNode(5,TreeNode(1),TreeNode(4,TreeNode(3),TreeNode(6)))
print(Solution().isValidBST(tree))