list = [1,2,3,45,5]
print(list[:])
num = 45
j = 0
for i in list:
    if num == i:
        list.pop(j)
        break
    j = j + 1
    print(j)

print(list[:])
