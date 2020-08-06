# Bubble Sort - In rgis we bubble up the largest element by swapping the elements from left to right.
# We check the elements from left to right and if greater element than we swap it. 

def bubblesort(arr ,n):
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
    print(arr);

arr=list(map(int,input().split()));
n = len(arr);
bubblesort(arr,n);
