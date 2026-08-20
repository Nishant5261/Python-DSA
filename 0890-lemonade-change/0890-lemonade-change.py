class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        j=0
        d={5:0,10:0,20:0}
        while j<len(bills):
            if bills[j]==5:
                d[5]+=1
                j+=1
            elif bills[j]>5:
                d[bills[j]]+=1
                change=bills[j]-5
                while change>0:
                    if change>10 and d[10]>0:
                        change-=10
                        d[10]-=1
                    elif change>=5 and d[5]>0:
                        change-=5
                        d[5]-=1
                    else:
                        return False
                j+=1
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna