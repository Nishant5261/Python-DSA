class Solution:
    def minimumCost(self, nums, k):
        mod=10**9+7
        z=sum(nums)
        n=(z//k)
        
        if z==k:
            return 0
        elif z%k==0:
            n-=1
        cost=int((n*(n+1))//2)
        
        return cost % mod

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna