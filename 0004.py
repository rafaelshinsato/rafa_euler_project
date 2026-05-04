largest_palindrome = 0
a = 999

while a >= 100:
    if a % 11 == 0:
        b = 999
        db = 1
    else:
        b = 990
        db = 11
    while b >= a:
        if a * b <= largest_palindrome:
            break
        curr = str(a * b)
        half = int(len(curr)/2)
        if curr[:half] == curr[:half-1:-1]:
            largest_palindrome = a * b

        b = b - db
    a = a - 1
print(largest_palindrome)

