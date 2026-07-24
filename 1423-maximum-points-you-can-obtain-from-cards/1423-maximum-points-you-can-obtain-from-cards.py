class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        ls,rs=0,0
        for i in range(k):
            ls+=cardPoints[i]
        m=ls
        ri=n-1
        for i in range(k-1,-1,-1):
            ls-=cardPoints[i]
            rs+=cardPoints[ri]
            m=max(m,ls+rs)
            ri-=1
        return m


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna