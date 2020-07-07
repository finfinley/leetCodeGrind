nums = [0,1,2,2,3,0,4,2]
val = 2
print(nums.count(val))
while nums.count(val): # count method returns the number of elements with the specified value
    nums.remove(val)
print(nums)
