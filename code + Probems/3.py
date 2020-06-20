N = int(input())
i = 0
dr = list()
while i < N:
    tr = input().split()

    if tr[0] == "insert":

        dr.insert(int(tr[1]), int(tr[2]))
    elif tr[0] == "print":
        print(dr)
    elif tr[0] == "remove":
        dr.remove(int(tr[1]))
    elif tr[0] == "append":
        dr.append(int(tr[1]))
    elif tr[0] == "sort":
        dr.sort()
    elif tr[0] == "pop":
        dr.pop()
    elif tr[0] == "reverse":
        dr.reverse()
    tr.clear()
    i += 1
