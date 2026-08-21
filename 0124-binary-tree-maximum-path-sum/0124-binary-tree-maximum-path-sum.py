# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def msum(self,root,sarr):
        if root==None:
            return 0
        ls=self.msum(root.left,sarr)
        if ls<0:
            ls=0
        rs=self.msum(root.right,sarr)
        if rs<0:
            rs=0
        sarr[0]=max(sarr[0],(root.val+ls+rs))
        return root.val+max(ls,rs)
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sarr=[float("-inf")]
        self.msum(root,sarr)
        return sarr[0] 
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna