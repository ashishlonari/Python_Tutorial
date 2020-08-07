# Insertion Sort

# Insertion Sort - So it is called as insertion sort as we take one element from unsorted list and insert into sorted list. So it is called as insertion sort.
def insertion(a,n):
    for i in range(1,n):
        temp = a[i];
        j=i-1;
        while j>=0 and a[j]>temp:
            a[j+1] = a[j];
            j=j-1;
        a[j+1]=temp;
    print(a);

a =list(map(int,input().split()));
n=len(a);
insertion(a,n);