A = [3,1,2,4,]
N = len(A)
i = 0 # slow pointer (Stays at the beginning of the array, only moves when new even int is moved to beginning 
j = 0 # fast pointer, goes to the next number in array each time 


while j < N: # while the pointer is still inside the array
    if A[j] % 2 == 0: # if the number (j) is even
        A[i],A[j] = A[j], A[i] # i switches places with j meaning j goes to the front of the array, and int at i goes to the end
        i +=1 # moves i to the next int because i is even now 
    j +=1 # always moves the fast pointer, j 
print(A)


