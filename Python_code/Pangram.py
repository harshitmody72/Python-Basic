import string

count = 0
s = input('Enter a string: ').lower()
li = [0] * 26
for i in s:
    if i in string.ascii_letters:
        li[ord(i) - 97] += 1

print(li)

for i in li:
    if i == 0:
        print('Not Pangram')
        break
else:
    print('Pangram')

#Enter a string: A quick brown fox jumps over the lazy dog