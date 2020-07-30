# Taking Multiple inputs in same line .
# So if we want to take multiple inputs in same line we use split method 
# This splits the input by space


x,y,z =input("Enter three values").split();
print("Number of Boys are :",x);
print("Number of Girls are :",y);
print("Number of Teachers are :",z);

# List Compreshension
# Pythn program taking multiple inputs with list compreshension

x = [int(x) for x in input("Enter Multiple Values").split()]
y=sum(x);
print("Number of list are ",x);
print("Sum Of list is ",y);

# Output
# USERs-MacBook-Air:Python_Tutorial ashish$ python3 Takingmultipleinputfromuser.py 
# Enter three values5 65 4
# Number of Boys are : 5
# Number of Girls are : 65
# Number of Teachers are : 4
# Enter Multiple Values4 6 4 95 75 75 45 354 75 84
# Number of list are  [4, 6, 4, 95, 75, 75, 45, 354, 75, 84]
# Sum Of list is  817