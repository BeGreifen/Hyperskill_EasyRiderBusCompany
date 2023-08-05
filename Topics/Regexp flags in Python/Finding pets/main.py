import re 

pattern = r"(dog|cat|parrot|hamster)"
string = input()
# your code here
print(re.findall(pattern, string, flags=re.IGNORECASE))
