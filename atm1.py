dic = {'1234':"Utsav",'2345':"Pandya"}
dic1 = {"Utsav":12345,"Pandya":76643}

try:
    def atm():
        pinno = str(input("Enter PIN No."))
        action = str(input(f"{dic[pinno]}, What you want do, draw or deposit money or check balance(draw,deposit,check):"))

        if action == "draw":
            enteramt = int(input("Enter Amount:"))
            if dic1[dic[pinno]]>enteramt:
                print("Transaction is being please wait.........")
                print("Transaction Completed Successfully!")
                newres = dic1[dic[pinno]] - enteramt
                dic1[dic[pinno]]= newres
                print(f"\nNew balace:{dic1[dic[pinno]]}")

                askq = str(input("\nWant to do anything more:"))
                if askq == 'yes':
                    atm()
                else:
                    print("......Thankyou.....")
                    exit()
            else:
                print("Check your balance first you idiot!")
                askq = str(input("\nWant to do anything more:"))
                if askq == 'yes':
                    atm()
                else:
                    print("......Thankyou.....")
                    exit()

        elif action == "deposit":
            print("\nEnter notes of 100,500,2000")
            note100 = int(input("Enter notes of 100(if not enter zero):"))
            note500 = int(input("Enter notes of 500(if not enter zero):"))
            note2000 = int(input("Enter no. of notes of 2000(if not enter zero):"))
            n100 = 100*note100
            n500 = 500*note500
            n2000 = 2000*note2000
            depamt = n100 + n500 + n2000
            print(f"Amount to be deposit is {depamt}")
            print("Successfully Deposited")
            dic1[dic[pinno]]= depamt

            askq = str(input("\nWant to do anything more:"))
            if askq == 'yes':
                atm()
            else:
                print("......Thankyou.....")
                exit()
        elif action == "check":
            print(f"{dic[pinno]}, Your Balance is {dic1[dic[pinno]]}")
            print("Thank you for using Atm Machine!")
            askq = str(input("\nWant to do anything more:"))
            if askq == 'yes':
                atm()
            else:
                print("......Thankyou.....")
                exit()

        else:
            print("Invalid Input")
            atm()

    atm()
            
except Exception as es:
    print("Invalid Pin")















# print("\n****ATM Machine***\n")
# pin = int(input("Enter PIN:"))
# if pin == 1234:
#     amt = int(input("\nEnter Amount"))
#     if amt > 50000:
#         pan = str(input("\nEnter PAN No.:")) 
#         if pan == "Str1234":
#             print("\nTrasaction Successful")
#             exit()
#     else : 
#         print("\nTransaction Successful")
# else :
#     print("Enter Correct PIN")
#     exit()
