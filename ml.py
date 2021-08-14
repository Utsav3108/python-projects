print("\n*******Think About any Vehicle(2-wheeler,4-wheeler,3-wheeler)*******")
print("\nAnswer in y or n\n")
rep = str(input("\nHave you think:"))
print(rep)
def ml():
    if rep == "y":
        r = str(input("\nYour vehicle has two Wheels?:"))
        if  r == "y":
            return ("Its 2-Wheeler Vehicle")
        else:
            res2 = str(input("Your Vehicle has 3-wheel?:"))
            if res2 == "y":
                return ("Its 3-wheeler Vehicle")
            else:
                res3 = str(input("Your Vehicle has 4-wheels?:"))
                if res3 == "y":
                    return ("Its 4-Wheelers Vehicle")
                else :
                    ml()
    else:
        pass
    
print(ml())
print("Program finished!")