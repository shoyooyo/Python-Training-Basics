x = "ajaz"

if "j" in x:
    if len(x) > 3:
        print(x, len(x))

#example 2 for the same

if ("j" in x) and (len(x) > 3):
    print(x, len(x))

#example 3 for a different calculation

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
    for j in list2:
        print(i*j)
    print(i)

#example for while

a = 1

while a <= 10:
    b = 5
    a += 1
    while b <=10:
            print(b)
            b += 1

#example for "forLoop"

for number in range(10):
    if 5 <= number <=9:
        print(number)