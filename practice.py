# arrc,element = list(map(int, input().split()));
# lst = list(map(int, input().split()));
# tmp = []
# for i in range(0,arrc):
#     if lst[i]==element:
#         temp=i+1;
#         tmp.append(temp);
# a=tmp.pop();
# print(a);

n_a = int(input())
a = sorted(list(map(int,input().split())))
n_b = int(input())
b = sorted(list(map(int,input().split())))
c = set()
# b[-1] and a[-1] is used to get the last element in the list
x = b[-1] - a[-1]
c = list(range(1,x+1))

for i in range(len(c)):
    for j in a:
        if c[i]+j not in b:
            c[i] = "x"
            break

for i in c:
    if i!="x":
        print(i, end = " ")