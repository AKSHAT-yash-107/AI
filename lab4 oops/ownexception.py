class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Access granted")


try:
    age = int(input("enter age"))
    check_age(age)
except InvalidAgeError as e:
    print("Custom Exception:", e)
