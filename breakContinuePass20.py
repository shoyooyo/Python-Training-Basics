#what is happening in the below piece of code
    #statement 1: we define range(10) // which if converted to list is 0 - 9
    #statement 1: we take each number of the range i.e., starting from 0
    #statement 2: compare the number 0 if is equal to 7 //which is not
    #statement 2: as statement is false, it goes to statement 4 skipping statement 3
    #statement 4: print the number which is 0

    #this goes on until number 7 arrives

for number in range(10):
    if number == 7:
        break
    print(number)

print("example 2 starts here")
print("======================")
print("   talks about break  ")
print("======================")

#example 2

list1 = [4,5,6]
list2 = [10,20,30]

for i in list1:
    for j in list2:
        if j == 20:
            break
        print(i)
        print(j)
        print(i*j)
    print("outside the nested loop")
print("main if block is stopped")

print("example 3 starts here")
print("======================")
print(" talks about continue ")
print("======================")

for i in list1:
    for j in list2:
        if j == 20:
            continue
        print(i)
        print(j)
        print(i*j)
    print("outside the nested loop")
print("main if block is stopped")

print("example 4 starts here")
print("==================")
print(" talks about pass ")
print("==================")

for abc in range(10):
    pass