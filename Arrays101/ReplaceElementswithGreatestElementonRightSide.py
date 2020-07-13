arr = [17,18,5,4,6,1]
N = len(arr)
ans=[]
for i in range(N-1):
    arr_r = max(arr[i+1:]) # Working through the array, finding the max as it goes and putting it into var arr_r
    ans.append(arr_r) # adds the max number from the right to the new array, ans 
ans.append(-1) # at the end of list, adds the -1
print(ans)
    
