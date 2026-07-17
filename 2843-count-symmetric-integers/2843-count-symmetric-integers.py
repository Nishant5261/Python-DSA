class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        c=0
        for i in range(low,high+1):
            n=str(i)
            z=list(map(int,n))
            l=len(z)
            if l%2!=0:
                continue
            if sum(z[:l//2])==sum(z[l//2:]):
                c+=1
        return c
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna