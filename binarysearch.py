# Binary Search - Divide and Conquer technique.

# Binary Search has one prequisite that in this the series of array must be sorted.

# If not sorted then we have to first sort the array and then apply Binary Search on that Array.

# def binary_search(arrlist,len_arr,element):
#     l = 0; 
#     r = len_arr-1;
#     while(l<r):
#         mid=int((l+r)/2);
#         if arrlist[mid]==element:
#             print("Element at Index ",mid);
#             break;
#         elif element<arrlist[mid]:
#             r=mid-1;
#         else:
#             l=mid+1;    
#     return -1;
# arrlist=list(map(int,input().split()));
# len_arr=len(arrlist);
# element=int(input("Element To Searched"));
# binary_search(arrlist,len_arr,element);


def binary_search(arrlist,len_arr,element):
    l = 0; 
    r = len_arr-1;
    mid=int((l+r)/2);
    lst =[];
    if arrlist[mid]==element:
        for i in range(0,mid+1):
            lst=arrlist[i];
        print(lst)
        print(sum(lst));
        
arrlist = list(map(int,input().split()));
len_arr = len(arrlist);
element = int(input("Enter Power"));
binary_search(arrlist,len_arr,element);

