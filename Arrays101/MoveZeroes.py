nums = [0,1,0,3,12]
val = 0

for i in nums:
    if nums.count(val):
        nums.remove(val)
        nums.append(val)
print(nums)