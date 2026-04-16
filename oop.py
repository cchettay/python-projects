class students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(self.name, "is studying")

    def info(self):
        print("Name", self.name)
        print("Age", self.age)
        print("Grade", self.grade)


student_1 = students("sam", 24, 6)
student_2 = students("cin", 24, 6)

student_1.study()
student_1.info()

student_2.study()
student_2.info()
