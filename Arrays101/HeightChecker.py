heights = [5,1,2,3,4]
N = len(heights)
sortedHeights = sorted(heights) # sorts heights
moves = 0 # initalize moves counter
i = 0 # heights pointer
j = 0 # sortedHeights pointer

while i < N: 
    if heights[i] != sortedHeights[j]: # if current position in heights does not match sortedHeights
        moves += 1 # add 1 to the moves counter
    i +=1 # keep the heights pointer moving
    j +=1 # keep the sortedHeights pointer moving 
print(moves)
    
        
