class Employee:
    percent_raise = 20

    def __init__(self, name, age, wage):
        self.name = name
        self.age = age
        self.wage = wage

    def wage_raise(self):
        self.wage = int(self.wage * self.percent_raise)


emp_1 = Employee("sam", 20, 5000)
emp_2 = Employee("ch", 30, 8990)
print(emp_1.wage)
emp_1.wage_raise()
print(emp_1.wage)
