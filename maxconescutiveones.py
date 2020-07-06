# Creates num array
nums =[1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]
# Creates empty string g
g = "";
print(nums)

# iliterate through array nums for ith time 
for i in nums:
    g = g+str(i) # adds str(i) to string g
print(g)
e = g.split('0') # Splits string at the zeros to make two seperate lists

# list e = ['11', '', '111', '11111111', '1', '']
max = 0;
n = 1;
print("e: ", e)
for i in e: # for ith item in list e
    if(max<len(i)): # if max is less than the length of item in list e
        print("Current max on " + str(n) + "th attempt: ", max )
        print(len(i))
        max=len(i) # the new max is now the length of items in list e
        n += 1
print("Max amount of consecutive ones: ", max)


