x,y = map(int,input().split())
z=0
for i in range(x):
    n1 = int(input("Enter no.:"))
    if n1%y==0:
        z += 1
print(z)

"""# x,y = map(int,input().split())
# n = []

# for i in range(x):
#     n1 = int(input("Enter no.:"))
#     n.append(n1)

# z=0
# for j in n:
#     if j%y==0:
#         z += 1
# print(z)
"""