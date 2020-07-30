# For Loop

a = [1,2,3,4,5,6,7,8];
for i in a:
    print(i); 
print();

# While Loop

while a:
    print(a.pop());

j=0;
b="Ashish like to play cricket";
while j<len(b):
    if b[j]=='s' or b[j]=='l':
        j += 1;
        continue;
    print(b[j]);
    j+=1;  

k=0
c="Common Boys you are the best";
while k<len(c):
    if c[k]=='B':
        k+=1;
        break;
    print(c[k]);
    k+=1; 