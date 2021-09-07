# # Loops

for i in range(5):
    print(i)

count = 0;
while count < 5:
    print(count)
    count += 1


for i in range(15):
    if i == 5:
        print("Countine -----------------------------", i)
        continue
    if i == 10:
        print("Break --------------------------------", i)
        break
    print("running ------------------------------", i)


for i in range(3):
    for j in range(3):
        print(f"({i},{j})")


count = sum = 0

while count < 5:
    val = eval(input('Enter number: '))
    if val < 0:
        print('Negative numbers not acceptable! Terminating')
        break
    count += 1
    sum += val
else:
    print('Average =', sum/count)
