def Number_Staircase(n):
    for rows in range(1, n + 1):
        for numbers in range(1, rows + 1):
            print(numbers, end="")
        print()
        



n = int(input("Enter a number: "))
Number_Staircase(n)