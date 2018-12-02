
infile =open("input.txt")

inlist = []
for line in infile:
    inlist.append(int(line))
infile.close()

count =0
freq_list={}

i = 0

for x in range(200):
    i = i+1
    for y in inlist:
        count = count + int(y)

        if count in freq_list:

            #if freq_list[count] > 0:
            print freq_list.get(count)
            print count
            print i
            break
            #else:
            #    freq_list[count] = freq_list[count]+1

        else:
            freq_list[count] = 0




