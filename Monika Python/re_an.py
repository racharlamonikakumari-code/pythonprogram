import re
txt = "The rain in Spain"
matches = re.findall("[a-n]", txt)
print(matches)  # Output: ['a', 'i', 'i', 'a', 'i']