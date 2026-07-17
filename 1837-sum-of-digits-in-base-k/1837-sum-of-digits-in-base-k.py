class Solution:
        def sumBase(self, n, k):
            total = 0
            while n > 0:
                total += n % k   # get last digit
                n //= k          # remove last digit
            return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna