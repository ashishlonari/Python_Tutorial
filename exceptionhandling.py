
# try : try keyword is used for checking whether it gives an exception.
# catch : catch is excepytion caught and gives appropriate message for the erroe,

# Finally: Python provides a keyword finally, which is always executed after try and except block

try :
    marks = 100;
    a=100/0
    z=[1,2,3,4,5,6,7];
    print(z[8]);
except (ZeroDivisionError,IndexError):
    print("You are tryning to divide number by zero or your index is zero")
finally:
    print("this is always executed at the end")