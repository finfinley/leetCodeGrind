A = [-4,-1,0,3,10]

N = len(A)
i = 0
while i < N:
    squaredInt = A[i] * A[i]
    A[i] = squaredInt
    i +=1
print(sorted(A))