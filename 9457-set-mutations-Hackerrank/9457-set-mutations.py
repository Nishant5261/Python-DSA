if __name__ == '__main__':
    a = int(input())
    set_a = set(input().split())
    n = int(input())
    
    for i in range(n):
        match input().split()[0]:
            case "update":
                set_a.update(input().split())
            case "intersection_update":
                set_a.intersection_update(input().split())
            case "difference_update":
                set_a.difference_update(input().split())
            case "symmetric_difference_update":
                set_a.symmetric_difference_update(input().split())
    
    print(sum(map(int,set_a)))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna