list = [5,7,9,3,1,0]
def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,6):
            if list[j]<list[minpos]:
                minpos = j
        x = list[i]
        list[i] = list[minpos]
        list[minpos] = x
        print(list)
sort(list)

print(list)



l_j = 60
l_min = 50

y = l_j
l_j = l_min
l_min = y
print("Swaped",l_j,l_min)