from array import array

m = array('H', [0]) * 10001
count = 0
for i in range(11, 10001):
    if i < 100 and i % 11 == 0:
        count += 1
    elif i > 1000:
        i0 = i % 10
        i1 = (i % 100) // 10
        i2 = (i % 1000) // 100
        i3 = i // 1000
        if i0 + i1 == i2 + i3:
            count += 1
    m[i] = count

class Solution:
    def countSymmetricIntegers(self, l, h):
        return m[h] - m[l - 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna