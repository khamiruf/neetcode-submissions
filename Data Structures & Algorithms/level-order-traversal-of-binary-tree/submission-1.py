# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return

            # If visiting this depth level for the first time, initialize a new sublist
            if level == len(res):
                res.append([])

            # Append the current node's value to its corresponding level list
            res[level].append(node.val)

            # Recurse left and right with incremented level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return res
