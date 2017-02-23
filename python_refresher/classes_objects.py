# Dictionary
lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 45, 65, 23, 22)
}

#Class: Object used to store data
class LotteryPlayer:
    def __init__(self, name):
        self.name = 'Rolf',
        self.numbers = (13, 45, 65, 23, 22)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")

print player_one == player_two  # False: instances/Pointers are different
                                # Two different entities that share the same signature
print player_one.name
print player_two.name
print player_one.name == player_two.name         # True: name is assigned on both

player_one.numbers = (1,2,3,6,7,8)

print player_one.numbers == player_two.numbers   # False: numbers assigned are different


## A Student Class

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average_grade(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print "I'm going to school"

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
anna.marks.append(36)
anna.marks.append(96)
print anna.average_grade()
print Student.go_to_school()