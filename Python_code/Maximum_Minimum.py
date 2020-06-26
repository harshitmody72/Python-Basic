largest = None
new = list()
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        num = int(num)
        new.append(num)
    except:
        print("Invalid input")


largest = max(new)
smallest = min(new)
print("Maximum is ", largest)
print("Minimum is ", smallest)