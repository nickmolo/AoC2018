from itertools import groupby 
import difflib


inlist = []
for line in open("input.txt"):
    inlist.append(line.rstrip())

index = -1
diclist = {}

for x in inlist:

    index = index +1
    groups =[]
    uniquekeys=[]
    for k,g in groupby(sorted(x)):
        groups.append(list(g))
        uniquekeys.append(k)

    diclist[index] = []
    for y in groups:
        if len(y) >1:
            diclist[index].append(len(y))


count2 =0
count3 =0

for k,v in diclist.iteritems():
    for x in sorted(set(v)):
        if x ==2:
            count2 = count2+1
        if x==3:
            count3=count3+1


print "part one solution %d" % (count2*count3)


#start of part 2

for x in inlist:
    for y in inlist:
        diff =0
        for i in zip(x,y):
            if i[0] != i[1]:
                diff = diff +1

        if diff ==1:
                
            print x
            print y
            exit()

