def number_pyramid(n):
    for rows in range(1, n+1):
        for numbers in range(1, rows + 1):
            counter = 0
            print(" " * (n - rows), numbers, end="")
        print()



n = int(input("Enter a number: "))
number_pyramid(n)