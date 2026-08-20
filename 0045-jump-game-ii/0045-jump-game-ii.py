class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps=0
        l=0
        r=0
        while r<len(nums)-1:
            nr=r
            for i in range(l,r+1):
                nr=max(nr,nums[i]+i)
            l=r+1
            r=nr
            jumps+=1
        return jumps

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna