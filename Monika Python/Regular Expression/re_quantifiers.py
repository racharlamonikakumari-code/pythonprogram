import re

text = "aaaaa"
result = re.findall(r'a?', text)
print(result)  # Output: ['', 'a', 'a', 'a', 'a', 'a', ''] (includes empty matches)