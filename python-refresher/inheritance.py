class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, **kwargs):
        return cls(friend_name, origin.school, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent("Anna", "Oxford", 20, "Software Developer")
print(anna.salary)
beatrice = Student("Bia", "MIT")

# friend = beatrice.friend(beatrice, "Lua", 10)

friend2 = WorkingStudent.friend(anna, "Mark", salary=15, job_title="Software Developer")
# print(friend.name)
# print(friend.school)
print(friend2.name)
print(friend2.school)
print(friend2.salary)
print(friend2.job_title)
