def largest_prime_factor(n):
    largest_prime = -1
    
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    while n % 3 == 0:
        largest_prime = 3
        n = n // 3
    
    i = 5
    
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i
        while n % (i + 2) == 0:
            largest_prime = i + 2
            n = n // (i + 2)
        i = i + 6

    if i > 4:
        largest_prime = n

    return largest_prime

print(largest_prime_factor(600851475143))
