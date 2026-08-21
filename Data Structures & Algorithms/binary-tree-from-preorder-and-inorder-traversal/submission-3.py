# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre = NLR
        # in = LNR
        # pre = [1,2,3,4], in = [2,1,3,4]
        # pre[0] --> always the root, 
        # then find the root in inorder and anything to the left is the left subtree
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            if in_left > in_right:
                return None
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            midpoint = inorder_map[root_val]

            root.left = helper(in_left, midpoint -1)
            root.right = helper(midpoint + 1, in_right)
            return root

        return helper(0, len(inorder) -1)