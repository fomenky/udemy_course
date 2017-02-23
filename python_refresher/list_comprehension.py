my_list = [0, 1, 2, 3, 4]
comprehensive_list = [x for x in range(5)]      # [0, 1, 2, 3, 4]

multiply_list =  [x * 3 for x in range(5)]
print multiply_list

print 8 % 3     # 8 / 3 == 6r2, so 8 % 3 == 2
print 9 % 3     # 9 / 3 == 3r0, so 9 % 3 == 0
print [n for n in range(10) if n % 2 == 0]  # [0, 2, 4, 6, 8]

people_you_know = ["Rolf", " John", "anna", "GREG"]
normalized_people = [person.strip().lower() for person in people_you_know]
print normalized_people

# SEE if_statements to make adjustments to code

def who_do_you_know():
    people = raw_input("Enter a comma-separated list of people you know: ")
    people_without_spaces = [person.strip() for person in people.split(",")]

    return people_without_spaces


def ask_user():
    person = raw_input("Now, enter a name: ")

    if person in who_do_you_know():
        print "You know this person"

    else:
        print "You don't know this person"


ask_user()