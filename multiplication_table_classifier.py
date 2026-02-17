def multiplication_table(n):
    even_count = 0
    odd_count = 0
    for i in range(1, 11):
        current_number = i * n
        if current_number % 2 == 0:
            even_count += 1
            print(f"{current_number} even")
        else:
            odd_count += 1
            print(f"{current_number} odd")
    print(f"Even: {even_count}  Odd: {odd_count}")





n = int(input("Enter a number: "))
multiplication_table(n)