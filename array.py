
a=[4,'Ashish',[1,2,33,45,6],'Suyog',87];
for i in range(0,5):
    print(a[i] ,end=" ");
print()

print(a[2][2]);

a.append(89);
print(a)


# USERs-MacBook-Air:Python_Tutorial ashish$ python3 array.py
# 4 Ashish [1, 2, 33, 45, 6] Suyog 87 
# 33
# [4, 'Ashish', [1, 2, 33, 45, 6], 'Suyog', 87, 89]
# USERs-MacBook-Air:Python_Tutorial ashish$ 