# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node, vals):
            if not node: 
                return None

            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)

        val = []
        inorder(root, val)
        return val[k-1]