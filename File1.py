# X = 40      # Money Pooja wants to withdraw
# Y = 1500.00 # Pooja's bank balance
# bank_charges = 0.5
# def atm():
#     if X%5==0:
#         total_amt_withdrawn = X + bank_charges
#         if total_amt_withdrawn<Y:
#             New_balance = Y - total_amt_withdrawn
#             return New_balance
#         else:
#             return Y
        
#     else:
#         print("Transaction not posible")

# print(atm())


# x,y = map(float, input().split())
# print(x,y)
# if x <= y-0.5 and x % 5==0:
#     print("%.2f"%(y-x-0.50))
# else:
#     print("%.2f"%y)

x,y = map(float,input().split())

if x>y or x%5!=0:
    print("Transaction Failed!")
else:
    y = y - x - 0.5
print(f"Amount balance:{'%.2f'%y}")
        

