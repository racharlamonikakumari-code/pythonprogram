import re
txt = "2026 is a year"
matches = re.findall("[0123]", txt)
print(matches)  # Output: ['2', '0', '2', '3']