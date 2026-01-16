class Sub1:
    def first(self):
        print("This is the first function from Sub 1 class")


class Sub2:
    def second(self):
        print("This is the second function from the Sub 2 class")


class Super(Sub1, Sub2):
    def final(self):
        print("This is the final method from the super class")


# Creating object of Super class
obj = Super()

# Calling all methods
obj.first()
obj.second()
obj.final()
