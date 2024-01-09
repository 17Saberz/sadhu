def check_FizzBuzz(data, score):
    if data % 3 == 0 and data % 5 == 0:
        return score + (data % 8)
    elif data % 3 == 0 or data % 5 ==0:
        return score + (data % 4)
    else:
        return score + (data % 10)

print("Welcome to FizzBuzz Game")

score = 0
while score <= 20:
    user = int(input("Enter number: "))
    score = check_FizzBuzz(user, score)

final_score = score % user
print("Your score: {}".format(final_score))