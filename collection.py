from collections import Counter
import collections;
print Counter(['A','A','B','C','B','C','A','C']);
print Counter({'A':8,'B':12,'C':4});
print Counter(A=4,B=8,C=13);
coun = Counter();
coun.update(['C','D']);
print(coun);


# Deque in python
# Deque is Doubly ended Queue in which we can insert and remove elements from both the sides.

print("==============================")
de =collections.deque([1,2,3,3,4,3,5,3,5])
print(de);
de.appendleft(8);
print(de);
de.append(9);
print(de);
c=de.count(3)
print("Number of 3 's in queue :",c);
de.reverse();
print(de);