A = [-4,-1,0,3,10]
temp = []

for i in A:
    squaredInt = i * i
    temp.append(squaredInt)
A = sorted(temp)
print(A)