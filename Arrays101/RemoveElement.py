nums = [0,1,2,2,3,0,4,2]
val = 2

# count method returns the number of elements with the specified value
while nums.count(val): # will loop through nums while val is in nums
    nums.remove(val) # removes val from nums while val is in nums (while loop, see above)
print(nums)
