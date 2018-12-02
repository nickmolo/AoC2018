
infile =open("input.txt")

count =0
for line in infile:
    count = count + int(line)


print count
