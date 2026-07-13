# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

x, M = map(int, input().split())

new_list = []

for _ in range(x):
    values = list(map(int, input().split()))
    my_list = values[1:]
    squared_list = [each*each for each in my_list] 
    new_list.append(squared_list)

print(max(sum(combo) % M for combo in product(*new_list)))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna