# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root,di):
        global mo
        if root==None:
            return
        self.dfs(root.left,di)
        if root.val in di:
            di[root.val]+=1
            mo=max(mo,di[root.val])
        else:
            di[root.val]=1
            mo=max(mo,di[root.val])
        self.dfs(root.right,di)
        return
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        global mo
        di={}
        ans=[]
        mo=float("-inf")
        self.dfs(root,di)
        
        for item in di.items():
            if item[1]>=mo:
                ans.append(item[0])
        return ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna