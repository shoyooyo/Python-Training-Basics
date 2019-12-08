x = 5
if x > 5:
    print("x is greater than 5")
    print(x*2)
elif x == 5:
    print("x is equal to 5")
else:
    print("x is not greater than 5")

print("===========================")
print("| Below used is with 'and'|")
print("===========================")

y = 10
if y == 5 and type(y) is int:
    print("y is integer and is equal to 5")
elif y == 10 and type(y) is int:
    print("y is integer and is equal to 10")