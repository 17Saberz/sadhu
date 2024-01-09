def check_equivalent(data):
    brackets = []
    for member in data:
        brackets.append(member)
    for i in brackets:
        if i == '(':
            if ')' in brackets:
                brackets.remove(i)
                brackets.remove(')')
            else:
                print("Not")

                
user = input("Bracket: ")

print(check_equivalent(user))