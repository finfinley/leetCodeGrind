nums1 = [1,2,3,0,0,0,0] # The zeros are space for merging num2 to array
m = 3 
nums2 = [2,5,6,1]
n = 4

print(nums1[:]) # just nums1 
print(nums1[:m]) # the first m numbers in array to merge from array nums1
print(nums2[:n]) # the first n numbers in array to merge from array nums2
nums1[:] = sorted(nums1[:m] + nums2[:n]) # takes both arrays and merges them together in num1 as a completely new object
print('nums1 array: ', nums1)


