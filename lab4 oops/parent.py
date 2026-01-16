# Parent class
class Parent:
    def fun1(self):
        print("This is the message from the fun1")


# Child1 inherits Parent (for Question 4)
class Child1(Parent):
    def fun2(self):
        print("This is the message from the fun2")


# Child2 inherits Child1 (Question 4 requirement)
class Child2(Child1):
    def fun3(self):
        print("This is the message from the fun3")


# Child inherits Parent (for Question 5)
class Child(Parent):
    def fun2(self):
        print("This is the message from the fun2")


# Hybrid inherits Child (Question 5 requirement)
class Hybrid(Child):
    def fun3(self):
        print("This is the message from the fun3")


# ---- OBJECT CREATION & METHOD CALLS ----

print("---- Question 4 Output ----")
obj1 = Child2()
obj1.fun1()   # from Parent
obj1.fun2()   # from Child1
obj1.fun3()   # from Child2

print("\n---- Question 5 Output ----")
obj2 = Hybrid()
obj2.fun1()   # from Parent
obj2.fun2()   # from Child
obj2.fun3()   # from Hybrid
