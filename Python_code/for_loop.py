number = [1,982,3,455,5,67]
i =0
greater = 0
for count in number:
    if greater < number[i]:
        greater = number[i]
    i +=1
print(greater)