arr = [-2,0,10,-19,4,6,-8]
# i is current position in arr
# N is compare number 
# M is N * 2
# This is not a good approach but it does work 

result = False

N = M = 0

if (arr.count(0) > 1): # if the count of 0's in the array is more than 1
    result = True # it is true because of duplicate zeros

for i in arr: # for every element in arr
    if i != 0: # as long as it doesnt equal 0 (taken care of above)
        N = i # N will now equal arr[i]
        M = N * 2 # multiply that by 2 to get M

        if M in arr: # if M is in array
            result = True # return true
            break # break out of loop
print(result)



