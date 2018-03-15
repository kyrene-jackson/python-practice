# Warm up-3: sum_double
# Given two int values, return their sum.
# Unless the two values are the same,
# then return double their sum.


def sum_double(int_1, int_2):
    if int_1 != int_2:
        return int_1 + int_2
    return (int_1 + int_2) * 2


# Check
print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))


# Now refactor!
def sum_double_alt(a, b):
    sum = a + b
    if a == b:
        sum = sum * 2
    return sum


print(sum_double_alt(1, 2))
print(sum_double_alt(3, 2))
print(sum_double_alt(2, 2))
