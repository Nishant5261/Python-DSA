# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue=deque([(root,0)])
        result={}
        ans=[]
        while queue:
            t=len(queue)
            for _ in range(t):
                e,line=queue.popleft()
                result[line]=e.val
                if e.left:
                    queue.append((e.left,line+1))
                if e.right:
                    queue.append((e.right,line+1))
        for values in sorted(result.items()):
            ans.append(values[1])
        return ans


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna