vendors = ["CC","Google","Netflix","FB"]

for every_vendor in vendors:
    print(every_vendor)

random_string = "Google"

for letter in random_string:
    print(letter)

print(len(vendors))
print(list(range(5)))

for elements in range(len(vendors)):
    print(vendors[elements])

for index, elem in enumerate(vendors):
    print(index, elem)
else:
    print("all elements are completed")