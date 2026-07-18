
def gcd_euclidean(a, b):
    a, b = abs(a), abs(b)  
    while b != 0:
        a, b = b, a % b
    return a
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=min(nums)
        l=max(nums)
        return gcd_euclidean(s,l)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna