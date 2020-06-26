prices = list()


while True:
    prices.append(int(input("enter the price of good's : ")))
    tr = input("want to enter more value's (y)es or (n)o: ").lower()
    if tr == "n" :
        break
        
        
sum = 0

for items in prices:
        sum += items


print(f"total price : {sum}")


