def generate_operator(number):
    if number % 2 == 0:
        xnumber = number ^ ((number >> 2) & 0x3)
        return {
            0: "push",
            1: "pop",
            2: "pop",
            3: "head",
            4: "push",
            5: "close",
            6: "head",
            7: "push",
            8: "pop",
            9: "push",
            10: "pop",
            11: "close",
            12: "head",
        }[xnumber % 13]
    else:
        xnumber = number ^ ((number >> 3) & 0x7)
        return {
            0: "push",
            1: "push",
            2: "pop",
            3: "close",
            4: "push",
            5: "push",
            6: "head",
            7: "push",
            8: "pop",
            9: "push",
            10: "pop",
            11: "close",
            12: "push",
        }[xnumber % 13]

def main():
    stack = []

    while True:
        number = int(input("Enter number: "))

        if number % 2 == 0:
            xnumber = number ^ ((number >> 2) & 0x3)
        else:
            xnumber = number ^ ((number >> 3) & 0x7)

        operator = generate_operator(xnumber)

        if operator == "push":
            stack.append(number)
            print(f"Push: {number}")
        elif operator == "pop":
            if len(stack) > 0:
                popped = stack.pop()
                print(f"Pop: {popped}")
        elif operator == "head":
                if len(stack) > 0:
                    print(f"Head: {stack[-1]}")
        elif operator == "close":
            print("Close")
            break

        print(f"Stack: {stack}")

    print("End of program, Bye!")

if __name__ == "__main__":
    main()