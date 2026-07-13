#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
decoded_script = ""
for j in range(m):
    for i in range(n):
        decoded_script += matrix[i][j]
    
print(re.sub(r"(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])", " ", decoded_script))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna