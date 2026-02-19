import re
#re.match() – Checks for a match only at the beginning of the string.
result = re.match(r'\\D+', '$h123$ab56c')
print(result.group())  # Output: 123
