import re 
txt = "rain in Spain"
matches = re.findall("[^arn]", txt)
print(matches)  # Output: [' ', 'i', ' ', 'i', 'S', 'p', 'a', 'i']