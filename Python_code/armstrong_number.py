input_number = input('enter a number : ')
x= int(input_number)
count = int(len(input_number))
sum = 0
re = 0
while x!= 0:
    re = x % 10
    sum = sum + re ** count
    x = x//10
if int(input_number) == sum:
    print(f"{input_number} is armstrong")
else :
    print("not")
