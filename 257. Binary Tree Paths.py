# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        path = []
        def rec(root,prev):
            if root:
                prev += str(root.val) 
            if root.left:
                rec(root.left, prev + "->")
            if root.right:
                rec(root.right, prev + "->")
            if root.left is None and root.right is None:
                path.append(prev)
        
        rec(root, "")
        return path
