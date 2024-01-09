import re

input_string = "rgb14RGB12gg14bbbbbbb21"
pattern = re.compile(r'([a-zA-Z]+[0-9]+)')

matches = pattern.findall(input_string)

print(matches)