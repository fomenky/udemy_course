# should_continue = True
# if should_continue:
#     print 'hello'
#
# known_people = ['jon', 'anna', 'mary']
# person = raw_input("Enter the person you know: ")
#
#
# if person in known_people:
#     print "You know {}".format(person)
#
# # if person not in known_people:
# else:
#     print "You don't know {}".format(person)

# Exercise
def who_do_you_know():
    # Ask user for a list of people they know
    # Split the string into a list
    # Return that list

    people = raw_input("Enter a comma-separated list of people you know: ")
    people_list = people.split(",")
    chomped_people_list = []
    for person in people:
        chomped_people_list.append(person.strip())
    return chomped_people_list

def ask_user():
    # Ask User for a name
    # See if their name is in the list of people they know
    # Print out they know the person
    person = raw_input("Now, enter a name: ")

    if person in who_do_you_know():
        print "You know this person"

    else:
        print "You don't know this person"


ask_user()



