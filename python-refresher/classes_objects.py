lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}


class LoteryPlayer:
    def __init__(self, name, numbers):
        self.name = name,
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


player_one = LoteryPlayer('Rolf', (5, 9, 12, 3, 1, 21))
player_two = LoteryPlayer('John', (3, 10, 23, 9, 21, 1))

print(player_one.name == player_two.name)


##


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anna = Student('Anna', 'MIT')
anna.marks.append(25)
anna.marks.append(30)
anna.marks.append(35)
print(anna.average())