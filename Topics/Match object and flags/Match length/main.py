import re

template = r'are you ready??.?.?'

try:
    len_string = re.match(template, input()).end()
except AttributeError:
    len_string = 0
print(len_string)
