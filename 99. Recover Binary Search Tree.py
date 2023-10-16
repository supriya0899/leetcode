# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    first = None
    middle = None
    last = None


    def inorder(self, root):
        if root is None:
            return None
        
        self.inorder(root.left)

        if self.prev != None and self.prev.val > root.val:
            #if only one vilolation
            if self.first == None:
                self.first = self.prev
                self.middle = root
            #if there are two violations
            else:
                self.last = root
            
        self.prev = root
        self.inorder(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.inorder(root)

        if self.first and self.last: # when non adjacent
            self.first.val, self.last.val = self.last.val, self.first.val
        else: # when adjacent
            self.first.val, self.middle.val = self.middle.val, self.first.val

      


        
