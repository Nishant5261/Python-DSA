# Enter your code here. Read input from STDIN. Print output to STDOUT
tc = int(input())
for i in range(tc):
    ele_in_A = int(input())
    A = set((map(int,input().split())))
    ele_in_B = int(input())
    B = set((map(int,input().split())))

    print(A <= B)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna