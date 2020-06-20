if __name__ == '__main__':
    s = input()
    t = len(s)
    count = 0
    for i in range(t):
        if s[i].isalnum() == True:
            count += 1
            break

    if count >= 1:
        print(True)
    else:
        print(False)

    count = 0
    for i in range(t):
        if s[i].isalpha() == True:
            count += 1
            break

    if count >= 1:
        print(True)
    else:
        print(False)
    count = 0
    for i in range(t):
        if s[i].isdigit() == True:
            count += 1
            break

    if count >= 1:
        print(True)
    else:
        print(False)
    count = 0
    for i in range(t):
        if s[i].islower() == True:
            count += 1
            break

    if count >= 1:
        print(True)
    else:
        print(False)
    count = 0
    for i in range(t):
        if s[i].isupper() == True:
            count += 1
            break

    if count >= 1:
        print(True)
    else:
        print(False)




