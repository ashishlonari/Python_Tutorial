# Linear Search
# Time Complexiety Of Best Case O(1) Worst case O(n) .
# In linear search the array is beign searched from start to end or to the element .

lst = list(map(int, input("Enter Elements").split()));
element = int(input("Enter element to be searched"));
b=len(lst)
found=0;
for i in range(0,b):
    if lst[i]==element:
        print("Element found with index ",i);
        found=1
        break;

if found==0:
    print("Element not found");
