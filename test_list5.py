values = [[3,4,5,1],[33,6,1,2]]

v = values[0][0]
print(v)

for lst in values:
    print(lst)
    for element in lst:
        print(element)
        if v > element:
            v = element

print(v)

