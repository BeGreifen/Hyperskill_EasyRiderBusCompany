import re

pattern = r"\bs\w*\b"
print(re.findall(pattern, input()))
