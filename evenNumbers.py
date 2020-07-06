nums = [12,345,2,6,7896, 123444]
evens = 0; # emply slate for integers with an even number
for i in nums: # for item in list nums 
    if len(str(i)) % 2 == 0: # if length of string in item is divisible by 2
        print("i as a string: ", str(i))
        print("i as an int: ", i)
        evens+=1; # add 1 to the evens slate
print(evens)

