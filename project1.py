from pandas import *
countries = ['Srilanka','Pakistan','Afghanistan']


Name = []
strk = []
balls = []
runs = []
data = {
    'Name':Name,
    'Strike':strk,
    'Runs':runs,
    'Balls':balls,
    }
for i in countries:
    print(f'Stats in {i}')
    n = str(input("Name of Batsman:"))
    r = int(input("Runs Scored:"))
    b = int(input("Balls faced:"))
    s = (r/b)*100
    Name.append(n)
    runs.append(r)
    balls.append(b)
    strk.append(s)

print(Name,strk,runs,balls)

Tab = DataFrame(data,index = countries)
print(Tab)