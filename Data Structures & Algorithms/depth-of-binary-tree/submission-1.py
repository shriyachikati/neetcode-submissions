# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the root is None, return 0
        if not root:
            return 0

        output = 0

        # Use stack for breadth first search
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            output = max(output, depth)
            if node.right:
                stack.append([node.right, depth+1])
            if node.left:
                stack.append([node.left, depth+1])

        return output