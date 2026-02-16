def Sum_Calculator(input):
    total = 0
    while input > 0:
        total = total + input
        input -= 1
    print(total)
    return total


user_input = int(input("Enter a number to add: "))
Sum_Calculator(user_input)