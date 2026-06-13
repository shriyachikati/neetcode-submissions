# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Get the higher and lower numbers among p and q to make the search easier
        lower = min(p.val, q.val)
        higher = max(p.val, q.val)
        
        def recursive_search(node, p, q):
            # If p and q are in either sides of the tree, the current node would be the ancestor
            if (p <= node.val) and (q >= node.val):
                return node
            
            # If p and q are less than the current node, the ancestor lies on the left half of the tree/subtree
            if (p < node.val) and (q < node.val):
                return recursive_search(node.left, p, q)
            # If p and q are greater than the current node, the ancestor lies in the right half of the tree/subtree
            elif (p > node.val) and (q > node.val):
                return recursive_search(node.right, p, q)

        return recursive_search(root, lower, higher)