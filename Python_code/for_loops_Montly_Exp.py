# Expermenting with the for loop
monthlyExp=[12000.5,100,5.75,1648.21];
total=0;

for exp in monthlyExp:
    print("I Spent : ",exp);
    total=total+exp;

avg=total/4;
print("\nTotal Exp : ",total);
print("Avg Exp : ",avg);


#advanced
menu={'Idly':40,'vada':40,'Poori':50,'Coffee/tea':10};
for name,price in menu.items():
    print(name+" item costs : "+str(price)+" Rs");





# Experimenting with Random numbers

import random
#normal scenario
r1=random.random();
print("\nRandom : ",r1);

#choosing in the list
r2=random.choice([10,20,30,40,50,60]);
print("Choosing Random from a List : ",r2);

# getting random by specifying the range
r3=random.randint(1,1000);
print("Getting random from a range : ",r3);
print("\n");