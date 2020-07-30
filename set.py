# Set

# Set has unique elements and cant be repeated.It is modifiable and  represented inside {} 

set1 ={1,1,5,6,"Ashish",};
print(set1);

set1.add(7);
print(set1);

set1.remove(5);
print(set1);


# Output
# USERs-MacBook-Air:Python_Tutorial ashish$ python3 set.py
# {1, 'Ashish', 5, 6}
# {1, 5, 6, 7, 'Ashish'}
# {1, 6, 7, 'Ashish'}