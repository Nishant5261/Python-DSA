class Solution:
        def sumBase(self, n, k):
            if n==0:
                return 0
            else:
                return n%k +self.sumBase(n//k,k)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna