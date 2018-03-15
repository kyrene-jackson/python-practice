# Ask the user for a list of people they know
# Split the string into a list
# Return that list


def who_do_you_know():
    people = input("Enter the names of people you know separated by commas: ") # Kyrene, Will, Leah
    people_list = people.split(",") # ["Kyrene", "Will", "Leah"]

    people_without_spaces = [person.strip() for person in people_list.list(",")]

    return people_without_spaces


# Ask the user a name
# See if their name is in the list of people they know
# Print out that they know the person


def ask_user():
    person = input("Enter a name of someone you know: ") # kyrene
    if person in who_do_you_know():
        print("You know {}!".format(person))

ask_user()
