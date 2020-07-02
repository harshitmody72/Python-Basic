try:
    num = input("Enter a number: ")
    count = len(num)
    num = int(num)

except:
    print("Sorry , Wrong Input ")
    quit()


num1= num
sum = 0
i = 0
while i <= count and num1 != 0:
    sum = sum * 10
    sum = sum + (num1 % 10)
    num1 //= 10
    i +=1

if sum == num:
    print(num , " is Palindrome Number")

else:
    print(num , " is not a Palindrome Number")
