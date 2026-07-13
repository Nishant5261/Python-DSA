#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    string1=sorted(input())
    c=Counter(string1)
    x=(c.most_common(3))
    for key,value in x:
        print(key , value)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna