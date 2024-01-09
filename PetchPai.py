# print("Fireworks Counter")
# scores = dict()
# while (data := input("Enter color code: ")) != "END":
#     for i, a in enumerate(data):
#         if a.isdigit():
#             break
#         key = "".join(sorted(data[:i]))
#         if key not in scores:
#             scores[key] = 0
#         scores[key] += int(data[i:])
#         print(f"{key:5} -> {scores[key]:10}")
    
#     display_key = sorted(scores.keys())
#     print()
#     print("Fireworks Satatistic")
#     for key in display_key:
#         print(f"{key:5} -> {scores[key]:10}")

import re
import string

def convert_input(letters):
    letters_list = sorted(letters)
    letters_output = ''
    for member in letters_list:
        letters_output += member
    return letters_output

counting = {}
available_colors = ["R","G","B","W","Y","P","C","O","M"]
pattern = re.compile(r'([a-zA-Z]+[0-9]+)')
alpha_u = string.ascii_lowercase
alpha_l = string.ascii_lowercase

while True:
    users = input("Enter color code: ")
    if users.upper() == "END":
        break
    matches = pattern.findall(users)
    if matches == []:
        letters = "U"
        digits = int(users)
        color = convert_input(letters)

        if color not in counting:
            counting[color] = 0
        
        counting[color] += int(digits)

        print(f"{color:<6}->{counting[color]:>11}")
    for i in matches:
        letters = ""
        digits = ""
        for char in i:
            if char.isalpha():
                char = char.upper()
                if char in available_colors:
                    if char not in letters:
                        letters += char
                        if "U" in letters:
                            letters = "U"
                else:
                    letters = "U"
                    pass
            elif char.isdigit():
                digits += char

        color = convert_input(letters)

        if color not in counting:
            counting[color] = 0
        
        counting[color] += int(digits)

        print(f"{color:<6}->{counting[color]:>11}")

print()
print("Fireworks Statistic")
sorted_dict = dict(sorted(counting.items()))
for key in sorted_dict:
    print(f"{key:<6}->{sorted_dict[key]:>11}")