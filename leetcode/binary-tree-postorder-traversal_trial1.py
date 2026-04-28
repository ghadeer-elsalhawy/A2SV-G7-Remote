# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def p(root):
            if not root:
                return res
            p(root.left)
            p(root.right)
            res.append(root.val)
            return res
        return p(root)