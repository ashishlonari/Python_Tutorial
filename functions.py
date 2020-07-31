def evenOdd(x):
    if(x%2==0):
        print("Even");
    else:
        print("Odd");
evenOdd(132);

def swap(x,y):
    temp=x;
    x=y;
    y=temp;
x=12;
y=9;
swap(x,y);
print(x);
print(y);

# Default Function
def myfunc(x,y=50):
    print(x);
    print(y);
myfunc(12);
print()

# Varaiable length argument
def anylenfunc(*argvs):
    for a in argvs:
        print(a);
anylenfunc('Hello ashish','Good morning',12,43);
print()