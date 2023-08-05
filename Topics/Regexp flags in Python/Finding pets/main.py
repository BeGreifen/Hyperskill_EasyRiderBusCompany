import re 

pattern="(dog|cat|parrot|hamster)"
string = input()
# your code here
print(re.findall(pattern,input(),flags=re.IGNORECASE))
