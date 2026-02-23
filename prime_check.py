def primes(n):
    prime_count = 0
    for i in range(2, n + 1):
        prime_number = True
        for prime_checker in range(2, i):
            if i % prime_checker == 0:
                prime_number = False
        if prime_number == True:
            prime_count += 1
            print(f"prime number:  {i}")
    return prime_count

n = int(input("Enter a number: "))
primes(n)