class Employee:
    def __init__(self, name, salary):
       
        self.salary = salary
        self.name=name

    def __str__(self):
        
        return f"Name: {self.name}, Salary: {self.salary}"


emp = Employee("akshat", 50000)
print(emp)  