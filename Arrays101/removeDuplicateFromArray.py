nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]

# overwrite on j while i is different 
# i is the fast pointer
# j is a slow pointer to be used to compare 

N = len(nums)

#if N <= 1: return N

i = j = 1 # start at nums[1] for both

while i < N: # while i is less then the length of nums (Hasn't ran out of elements yet) 
    if nums[i] != nums[i-1]: # unique element found
        nums[j] = nums[i] # overwrite our slow pointer (j) with element found at num[i]
        j += 1 # Move slow pointer (j) to next element for comparison
    i += 1 # move fast pointer to next element each step
#return j



