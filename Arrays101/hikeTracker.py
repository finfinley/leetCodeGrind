s = 'DDUUDDUDUUUD'
n = 8
level = valley = 0

for i in range(n):
    if s[i] == 'U':
        level +=1 # level increases to 1 
        if level == 0: # if the hiker is at sea level. Only happens on the upclimb, because they have to climb out of a valley
            valley +=1 # they exited a valley 
    else:
        level -=1 # Going down
    
print(valley)
