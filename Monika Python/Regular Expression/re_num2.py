import re
txt = "The year is 2026"
matches = re.findall("[0-9]", txt)
print(matches)