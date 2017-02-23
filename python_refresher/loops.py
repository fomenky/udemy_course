my_variable = "hello"

# for loops
for character in my_variable:   # my_variable is an iterable: Ex are strings,lists,sets,tuples, dicts etc
    print character

my_list = [1,2,3,4,5]

for number in my_list:
    print number**2

# while loops
user_wants_number = True
while user_wants_number == True:
    print 10

    user_input = raw_input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False


