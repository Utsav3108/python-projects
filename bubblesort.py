#bubblesort
def sort(listt):
    for i in range(len(listt)-1,0,-1):
        for j in range(i):
            if listt[j]>listt[j+1]:
                x = listt[j+1]
                listt[j+1] = listt[j]
                listt[j] = x
    

print("Enter 5 no. to arrange them in assending order")

a,c,d,e,v  = input("Enter 5 no.:").split(',')
listt = [int(a),int(c),int(d),int(e),int(v)]
sort(listt)
print(listt)

