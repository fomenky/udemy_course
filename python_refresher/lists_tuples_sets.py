

grades = [77, 80, 90, 95, 100]              # List
tuple_grades = (77, 80, 90, 95, 100)        # Tuple: Tuples are IMMUTABLE!
set_grades = {77, 80, 90, 95, 100, 100}     # Set: unique & unordered

print (sum(grades) / len(grades))           # Average

grades.append(105)
# tuple_grades.append(105)                  # Won't work because tuples are immutable!
print (set_grades)                          # set([80, 90, 100, 77, 95])


# Operations
grades.append(102)
print (grades)

tuple_grades = tuple_grades + (102,)        # Correct way of appending to a tuple
print (tuple_grades)

set_grades.add(60)                          # Correct way of appending to a set
print (set_grades)

# tuple_grades[0] = 60                      # results to error since tuples are immutable
# set_grades[0] = 60                        # results to error since sets are unique & onordered


# #Advanced Set Operations
lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11 }


print lottery_numbers.intersection(winning_numbers)   # Check for matching numbers
print lottery_numbers.union(winning_numbers)          # union
print lottery_numbers.difference(winning_numbers)     # difference










