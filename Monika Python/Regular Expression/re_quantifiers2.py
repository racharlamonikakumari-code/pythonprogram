import re
text = "aaaaa"
result = re.findall(r'a{5}', text)
print(result)  # Output: ['aaa']

