# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #depth seems like dfs problem
        depth = 0
        
        if root is None:
            return depth
        else: 
            depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            return depth
                