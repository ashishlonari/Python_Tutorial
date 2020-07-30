# List 
# It is like an Array on C
# the list can contain data of different types.
# The items stored in the list are separated with a comma (,) and enclosed within square brackets []
# We can use slice [:] operators to access the data of the list

list1 = [1 , "Ashish" , "Vaibhav" , "Saurav" ,"Gaurav","Gnaesh","Suyog"];
print(list1);
print(list1[2]);
print(list1[3:]);
print(list1[:4]);
print(list1[3:6]);
print(list1 + list1);
print(len(list1));
print(list1 * 3);
list1.append("Swarrop");
print(list1);
print(list1.pop());


# Output

# USERs-MacBook-Air:Python_Tutorial ashish$ python3 list.py
# [1, 'Ashish', 'Vaibhav', 'Saurav', 'Gaurav', 'Gnaesh', 'Suyog']
# Vaibhav
# ['Saurav', 'Gaurav', 'Gnaesh', 'Suyog']
# [1, 'Ashish', 'Vaibhav', 'Saurav']
# ['Saurav', 'Gaurav', 'Gnaesh']
# [1, 'Ashish', 'Vaibhav', 'Saurav', 'Gaurav', 'Gnaesh', 'Suyog', 1, 'Ashish', 'Vaibhav', 'Saurav', 'Gaurav', 'Gnaesh', 'Suyog']
# 7
# [1, 'Ashish', 'Vaibhav', 'Saurav', 'Gaurav', 'Gnaesh', 'Suyog', 1, 'Ashish', 'Vaibhav', 'Saurav', 'Gaurav', 'Gnaesh', 'Suyog', 1, 'Ashish', 'Vaibhav', 'Saurav', 'Gaurav', 'Gnaesh', 'Suyog']
# [1, 'Ashish', 'Vaibhav', 'Saurav', 'Gaurav', 'Gnaesh', 'Suyog', 'Swarrop']
# Swarrop