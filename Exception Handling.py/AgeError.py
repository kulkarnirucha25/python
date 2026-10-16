class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age: "))

try:
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    elif age < 18:
        raise InvalidAgeError("You must be at least 18 years old")
    else:
        print("Age is valid")

except InvalidAgeError as e:
    print("InvalidAgeError:", e)