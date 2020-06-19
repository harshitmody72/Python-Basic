# gives the most common word in the file
# for loop

fnmae = input()
fhand = open(fnmae)
dr = dict()



for lines in fhand:
    lines = lines.rstrip()
    lines = lines.split()
    for i in lines:
        dr[i] = dr.get(i,0) +1

temp = None
kname = None


for k in dr:
    if temp == None or temp < dr[k]:
        temp = dr[k]
        kname = k


print(kname , temp)
