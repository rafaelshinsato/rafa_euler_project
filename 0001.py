def sum_multiple_of_two_numbers_less_than_x(a,b,x):
    # sum multiples of a, b less than x
    sum = 0
    for i in range(1,1000):
        if i % a == 0 or i % b == 0:
            sum = sum + i
    return sum

print(sum_multiple_of_two_numbers_less_than_x(3, 5, 1000))  # Print out the sum of multiples of 3 and 5 less than 1000

