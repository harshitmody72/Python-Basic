def swap_case(s):
    i =0
    tr = len(s)
    rt = ''
    while i< tr :
        if s[i].isupper() == True:
            rt += s[i].lower()
        elif s[i].islower() == True:
            rt += s[i].upper()
        elif s[i] == " ":
            rt += " "
        else :
            rt += s[i]

        i +=1

    return rt

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# Convert the case of string
# lower case ---> upper case
# vice versa
