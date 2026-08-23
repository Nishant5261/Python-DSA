# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deletion(self,node):
        if not node.left: return node.right
        elif not node.right: return node.left
        else:
            rc=node.right
            lr=self.findr(node.left)
            lr.right=rc
            return node.left
    def findr(self,node):
        while node.right:
            node=node.right
        return node
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root: return root
        if root.val==key: return self.deletion(root)
        temp=root
        while temp:
            if temp.val>key:
                if temp.left and temp.left.val==key:
                    temp.left=self.deletion(temp.left)
                else: temp=temp.left
            else:
                if temp.right and temp.right.val==key:
                    temp.right=self.deletion(temp.right)
                else: temp=temp.right
        return root


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna