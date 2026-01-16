class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return self.name


class B:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        return self.name


class C(A, B):
    def __init__(self, name, age, id):
        A.__init__(self, name, age)
        B.__init__(self, name, id)

    def get_details(self):
        return self.name


# Creating object of class C
obj = C("Akshat", 21, 101)
print(obj.get_details())
