def fib_sum_even_less_than_x(x):
    sum = 2
    fib1 = 2  # Can skip to the step after the first addition to the sum
    fib2 = 3
    while fib2 < x:
        # set up the next iteration of fib
        temp = fib1
        fib1 = fib2
        fib2 = temp + fib2
        if fib2 % 2 == 0:
            sum = sum + fib2
    return sum

print(fib_sum_even_less_than_x(4000000))

