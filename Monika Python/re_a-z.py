import re
txt = "Hello World 123!"
matches = re.findall("[a-zA-Z]", txt)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']