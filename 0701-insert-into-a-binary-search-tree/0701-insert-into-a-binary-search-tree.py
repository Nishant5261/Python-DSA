# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def search(self,root,val):
        if not root:
            return None
        if val>root.val:
            if root.right:
                return self.search(root.right,val)
            else:
                return root
        elif val<root.val:
            if root.left:
                return self.search(root.left,val)
            else:
                return root
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node=TreeNode(val)
        inode=self.search(root,val)
        if inode:
            if inode.val<val:
                inode.right=node
            else:
                inode.left=node
            return root
        else:
            return node

    
    
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna