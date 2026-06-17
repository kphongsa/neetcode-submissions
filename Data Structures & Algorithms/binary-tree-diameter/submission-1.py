# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    d = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #for any node, longest path = max height of left + right
        diameter = 0

        def height(root: Optional[Treenode]) -> int:
            nonlocal diameter

            if root is None:
                return 0
            else: 
                diameter = max(diameter, height(root.left) + height(root.right))
                return max(height(root.left), height(root.right)) + 1
                

        height(root)
        return diameter
