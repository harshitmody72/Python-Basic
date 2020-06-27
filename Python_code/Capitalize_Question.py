
#You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck

# a_string = input().split(' ')
# print(' '.join((word.capitalize() for word in a_string)))
# print(a_string)

s = input().split(' ')
i = 0
for j in s:
    s[i] = s[i].capitalize()
    print(s[i])
    i = i +1
tr = " ".join(s)
print(tr)
