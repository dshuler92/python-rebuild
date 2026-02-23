def reverse_stair(n):
    for rows in range(n, 0, -1):
        for numbers in range(1, rows + 1):
            print(numbers, end="")
        print()


n = int(input("Enter a number: "))
reverse_stair(n)