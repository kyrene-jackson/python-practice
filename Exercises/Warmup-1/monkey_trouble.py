# Warm up-2: monkey_trouble
# We have two monkeys, a and b and the
# parameters a_smile and b_smile indicate
# if each is smiling. We are in trouble
# if they are both smiling or if neither
# of them is smiling. Return True if we are
# in trouble.


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False


# Check
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))


# Now refactor!
def more_monkey_trouble(c_smile, d_smile):
    return c_smile == d_smile


print(more_monkey_trouble(True, True))
print(more_monkey_trouble(False, False))
print(more_monkey_trouble(True, False))



