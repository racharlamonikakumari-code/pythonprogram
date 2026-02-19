import re
result = re.sub(r'\d+', 'X', 'abc123def456')
print(result)  # Output: abcXdefX