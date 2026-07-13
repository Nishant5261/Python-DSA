import re

if __name__ == "__main__":
    n = int(input())
    html = "\n".join(input() for _ in range(n))
    html = re.sub(r'<!--.*?-->','',html,flags=re.DOTALL)
    tag_pattern = re.compile(r'<\s*(\w+)([^>]*)>')
    attr_pattern = re.compile(r'([\w-]+)\s*=\s*"([^"]*)"')
    for tag, attrs in tag_pattern.findall(html):
        print(tag)
        for key, value in attr_pattern.findall(attrs):
            print(f"-> {key} > {value}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna