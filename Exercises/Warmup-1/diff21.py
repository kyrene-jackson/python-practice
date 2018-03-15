# Warm up-3: diff21
# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.


def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


print(diff21(19))
print(diff21(10))
print(diff21(21))
