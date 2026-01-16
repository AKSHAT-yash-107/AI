class Employee:
    def __init__(self, name, salary):
      
        self.name = name
        self.salary=salary

    def __str__(self):
     
        return f"Name: {self.name}, Salary: {self.salary}"


emp = Employee("yesh",3 )
print(emp)  