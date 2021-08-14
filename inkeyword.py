num = int(input("Enter a No.:"))
listt = [3,4,5,6,7]
def sel(listt,num):
    for r in listt:
        if r == num:
            return ("Value Exist!")
    return ("Value doesnot Exist!")   

print(sel(listt,num))

if num in listt:
    print("Congrats!")
else :
    print("Get lost!")