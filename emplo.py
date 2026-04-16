class Employee:

    def __init__(self, name, age, wage):
        self.name = name
        self.age = age
        self.wage = wage


emp_1 = Employee("sam", 20, 5000)
emp_2 = Employee("ch", 30, 8990)

print(emp_1.name)
print(emp_2.wage)
