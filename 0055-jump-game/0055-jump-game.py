class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
        if nums[0]==0:
            return False
        mi=0
        for i in range(len(nums)-1):
            if i>mi:
                return False
            mi=max(mi,i+nums[i])
            if mi>=len(nums)-1:
                return True
        return False

            



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna