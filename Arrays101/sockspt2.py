ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

matches = 0

for i in ar:
    numSocks = ar.count(i) // 2
    matches += numSocks
    ar = list(filter((i).__ne__, ar))

print(matches)

