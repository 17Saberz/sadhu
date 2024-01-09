def check_word(words):
    count = 0
    checked = []
    for word in words:
        if word not in checked:
            checked.append(word)
            count += 1
    return count

def check_frequency(words):
    checked = {}
    for word in words:
        if word in checked:
            checked[word] += 1
        else:
            checked[word] = 1
    frequency = [checked[word] for word in checked]
    return frequency

num_word = int(input("Word = "))
words = []

for i in range(num_word):
    words.append(input(">>> "))

unique_word = check_word(words)
frequency = check_frequency(words)
output = ''

print("Ans =>")
print(unique_word)
for member in frequency:
    output += (str(member) + ' ')
print(output)