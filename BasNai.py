def convert_input(letters):
    letters_list = sorted(letters)
    letters_output = ''
    for member in letters_list:
        letters_output += member
    return letters_output

counting = {}
print("Fireworks Counter")
while True:
    users = input("Enter color code: ")
    if users == "END":
        break
    letters = ""
    digits = ""
    for char in users:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            digits += char

    color = convert_input(letters)
    if color in counting:
        counting[color] += int(digits)
    else:
        counting[color] = int(digits)

    print(f"{color:<6}->{counting[color]:>10}")

print()
print("Fireworks Statistic")
for key in counting:
    print(f"{key:<6}->{counting[key]:>10}")