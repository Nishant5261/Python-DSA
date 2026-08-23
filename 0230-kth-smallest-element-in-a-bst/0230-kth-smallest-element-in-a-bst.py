# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bfs(self,root,k,ans):
        if not root:
            return
        self.bfs(root.left,k,ans)
        if len(ans)==k:
            return
        ans.append(root.val)
        if len(ans)==k:
            return
        self.bfs(root.right,k,ans)
        return 
        
    def kthSmallest(self, root,k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ans=[]
        self.bfs(root,k,ans)
        return ans[-1]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna