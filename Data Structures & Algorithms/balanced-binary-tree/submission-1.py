# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root is None:
                return 0
            else: 
                return max(height(root.left), height(root.right))+ 1
        
        if (root is None): 
            return True
        
        left = height(root.left)
        right = height(root.right)

        print(left, right)

        balanced = (abs(left - right) <= 1)
        
        return (balanced and self.isBalanced(root.left) and self.isBalanced(root.right))