class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        ts=(len(word)*(len(word)+1)//2)
        c=0        
        for i in range(len(word)):
            ts=(len(word)*(len(word)+1))//2
            if word[i] in 'aeiou':
                ps=((i+1)*(i))//2
                ns=((len(word)-i-1)*(len(word)-i))//2
                c+=(ts-ps-ns)
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna