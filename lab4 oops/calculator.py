class Calculator:
   
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

  
    def execute_command(self, command, num1, num2):
        if command == 'add':
            return self.add(num1, num2)
        elif command == 'sub':
            return self.sub(num1, num2)
        elif command == 'mul':
            return self.mul(num1, num2)
        elif command == 'div':
            return self.div(num1, num2)
        else:
            return "Invalid Command"


calc = Calculator()
result = calc.execute_command('add', 10, 5)
print(f"Result of add: {result}")  

print(f"Result of mul: {calc.execute_command('mul', 10, 5)}") 