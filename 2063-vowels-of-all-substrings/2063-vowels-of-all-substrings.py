class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        c=0 
        l=len(word)          
        for i in range(len(word)):            
            if word[i] in 'aeiou':
                c+=(i+1)*(l-i)
                
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna