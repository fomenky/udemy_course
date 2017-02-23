class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        # Return a new student named "friend_name" in the same school as self
        return cls(friend_name, origin.school, salary)

##

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        # super().__init__(name, school)        # Python 3
        Student.__init__(self, name, school)    # Python 2
        self.salary = salary


anna = WorkingStudent("Anna", "Oxford", 20.00)
print anna.salary

friend = WorkingStudent.friend(anna, "Greg", 17.00)
print friend.name
print friend.school
#print friend.salary # Returns Error if @classmethod is not included
print friend.salary
