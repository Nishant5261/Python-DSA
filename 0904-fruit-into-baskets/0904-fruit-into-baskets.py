class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        s={}
        c=0
        l=0
        r=0
        while r<len(fruits):
            s[fruits[r]]=s.get(fruits[r],0)+1
            if len(s)>2:
                s[fruits[l]]-=1
                if s[fruits[l]]==0:
                    del s[fruits[l]]
                l+=1
            if len(s)<=2:
                c=max(c,r-l+1)
            r+=1
        return c

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna