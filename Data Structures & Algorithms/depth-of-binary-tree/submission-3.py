# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs
        if (root is None):
            return 0

        queue = [root]
        depth = 0

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
            
                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)

            depth += 1

        return depth