def get_total(menu, quantity):
    if menu == 1:
        return 7 * quantity
    elif menu == 2:
        return 13 * quantity
    elif menu == 3:
        return 9 * quantity
    elif menu == 4:
        return 3 * quantity
    elif menu == 5:
        return 5 * quantity
    
def check_money(total, money):
    while total > money:
        print("{} Bath left.".format(total - money))
        insert = int(input("Enter your money: "))
        money += insert
    changes = money - total
    if changes > 0:
        print("Change: {} Baht".format(changes))

    while changes > 0:

        if changes // 10 > 0:
            check_10 = changes // 10
            if check_10 > 1:
                print("   10: {} coins".format(check_10))
            else:
                print("   10: {} coin".format(check_10))
            changes -= (10*check_10)

        elif changes // 5 > 0:
            check_5 = changes // 5
            if check_5 > 1:
                print("   5: {} coins".format(check_5))
            else:
                print("   5: {} coin".format(check_5))
            changes -= (5*check_5)

        elif changes // 2 > 0:
            check_2 = changes // 2
            if check_2 > 1:
                print("   2: {} coins".format(check_2))
            else: 
                print("   2: {} coin".format(check_2))
            changes -= (2*check_2)

        elif changes // 1 > 0:
            check_1 = changes // 1
            if check_1 > 1:
                print("   1: {} coins".format(check_1))
            else:
                print("   1: {} coin".format(check_1))

    print("Thank you")

print("Kanom Machine")
print("  1. Khanom Jak             7 Baht")
print("  2. Khanom Kruy           13 Baht")
print("  3. Khanom Keemod          9 Baht")
print("  4. Khanom Co              3 Baht")
print("  5. Khanom Dokdon         22 Baht")

order = int(input("Enter your order: "))
quantity = int(input("Enter Quantity: "))
total = get_total(order, quantity)

print("Total: {}".format(total))

money = int(input("Enter your money: "))

check_money(total, money)