# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,root,p,q):
        if not root:
            return None
        if root==p or root==q:
            return root
        left=self.dfs(root.left,p,q)
        right=self.dfs(root.right,p,q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None

        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root,p,q)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna