class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        c=0
        l=0
        r=0
        z=0
        while r<len(nums):
            if nums[r]==0:
                z+=1
            if z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            if z<=k:
                c=max(c,r-l+1)
            r+=1
        return c
        

                    

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna