
try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print("Age can't be zero '0'")
except ValueError:
    print("Invalid age value")
finally:
    print("Thank You!!!")
