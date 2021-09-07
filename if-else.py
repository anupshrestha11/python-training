salary = eval(input("Enter Salary: "))

if(salary == 0):
    print("volunteer")
elif(salary <= 15000):
    print("intern")
elif(salary > 15000 and salary <= 35000):
    print("Employee")
elif(salary > 35000):
    print("Owner")
else:
    print("Invalid Input")
