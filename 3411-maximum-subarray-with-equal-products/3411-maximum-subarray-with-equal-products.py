class Solution:
    def maxLength(self, A ):
        N = len(A)
        ans = 2
        last = {}
        i = 0
        for j, x in enumerate(A):
            for p in prime_divisors(x):
                i = max(i, last.get(p, -1) + 1)
                last[p] = j
            ans = max(ans, j - i + 1)
        
        return ans

def prime_divisors(x):
    d = 2
    while d * d <= x:
        if x % d == 0:
            x //= d
            while x % d == 0:
                x //= d
            yield d
        d += 1 + d & 1
    
    if x > 1:
        yield x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna