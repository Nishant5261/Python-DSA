# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bfs(self,root,ans):
        
        if not root:
            return
        self.bfs(root.left,ans)
        
        ans.append(root.val)
        
        self.bfs(root.right,ans)
        return 
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans=[]
        self.bfs(root,ans)
        ans.sort()
        print(ans)
        sm=root.val
        for i in ans:
            if i>sm:
                return i
        return -1
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna