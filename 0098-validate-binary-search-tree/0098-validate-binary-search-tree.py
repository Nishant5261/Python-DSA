# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invalid(self,root,lr,rr):
        if root==None:
            return False
        if self.invalid(root.left,lr,root.val):
            return True
        if not(root.val>lr and root.val<rr):
            return True
        if self.invalid(root.right,root.val,rr):
            return True
        return False
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return not self.invalid(root,float("-inf"),float("inf"))

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna