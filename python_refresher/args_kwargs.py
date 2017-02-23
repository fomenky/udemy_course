#Without *args
def my_method(arg1, arg2):
    return arg1 + arg2

print my_method(1,2)


def addition_simplified(*args):
    return sum(args)

print addition_simplified(1,2)


##kwargs == keyword arguments

def what_are_kwargs(*args, **kwargs):
    print args
    print kwargs

what_are_kwargs(12, 34, 56, name='jose', location='UK')

# Looking back at our Student method
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        # Return a new student named "friend_name" in the same school as self
        return cls(friend_name, origin.school, *args, **kwargs)

##

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        # super().__init__(name, school)        # Python 3
        Student.__init__(self, name, school)    # Python 2
        self.salary = salary
        self.salary = job_title


anna = WorkingStudent("Anna", "Oxford", 20.00, "Software Developer")
print anna.salary

friend = WorkingStudent.friend(anna, "Greg", 17.00, job_title="Software Developer")
print friend.name
print friend.school
#print friend.salary # Returns Error if @classmethod is not included
print friend.salary


