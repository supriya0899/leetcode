# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = []

        def rec(root, l, h):
            if root:
                if root.val >= l and root.val <= h:
                    ans.append(root.val)
                
                if root.left:

                    rec(root.left, l, h)
                
                if root.right:
                    rec(root.right,l, h)
        
        rec(root, low, high)
        
        return sum(ans)
