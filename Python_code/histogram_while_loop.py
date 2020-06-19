## gives the most common word in the file
# it is in while loop

dr = dict()
i= 0
n = int(input("no of iteration: "))
temp =None
nt = None
while i<n:
    i +=1



    dname = input("Enter the words: ")
    if dname not in dr:
        dr[dname] = 1
    else:
        dr[dname] += 1


print(dr)
print(len(dr))
for key in dr:
    if temp == None:
        temp = dr[key]
        nt = key
    elif temp < dr[key]:
        temp = dr[key]
        nt = key

print(nt,temp)


