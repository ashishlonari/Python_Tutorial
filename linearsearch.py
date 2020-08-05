arr=[5,4,3,4,5,7,4,2,43,51];
arr1=list(map(int,input()).split());
element = int(input("Enter element to be searched"));
b=len(arr)
found=0;
for i in range(0,b):
    if arr[i]==element:
        print("Element found with index ",i);
        found=1
        break;

if found==0:
    print("Element not found");
