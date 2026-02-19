import re
txt = "rain in Spain"
matches = re.findall("[arn]", txt)
print(matches)  # Output: ['r', 'a', 'n', 'n', 'a', 'n']