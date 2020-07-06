
# Given a fixed length array arr of integers, duplicate each occurrence of zero, 
# shifting the remaining elements to the right.
# add a zero to any 
i = 0
arr = [1,0, 0, 2,3,0,4,5,0]
print(arr)

# While loop ensures we will only loop through the length of the array (arr)
while i < len(arr) - 1: # This code will run while the index is less than the length of the list (running as long as the list)
    if arr[i] == 0: # If the current index (i) of the list (arr) equals 0
        arr.insert(i+1,0) # adds zero after zero in list
        del arr[len(arr)-1] # Deletes the end of the list because list can only be as long as orginal array (arr)
        print(arr)
        i = i + 2 # Indexes two spaces ahead because we know the next index will be a zero
    else: 
        i = i + 1 # Index to the next index of the array (arr) to check and see if it equals 0
