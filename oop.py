
# Inheritance

# Inhritance: The properties of one class could be called in other class this proprty of OOP is called Inheritance.
# Due to inheritance code reusability is increased and a class could inherit the properties of other class .

class Person:
    def __init__(self,name):
        self.name=name;
    def empl(self):
        print(self.name,"Is not a employee");

class Employee(Person):
    def empl(self):
        print(self.name,"Is a Employee");
# So here person class is beign inherited in Employee class and we check whether the person is an employee or not .

e =Employee("Ashish");
e.empl();

p= Person("Suyog");
p.empl();
print("================================");


# Multiple Inheritance

# Multiple Inheritance is a condition when properties of two or more classes are inherited in class.

class Base1:
    def __init__(self,name,passion):
        self.name = name;
        self.passion = passion;
    def passion1(self):
        print("Name is ",self.name );
        print(self.name,"Passion is ",self.passion );

class Base2:
    def __init__(self,roll):
        self.roll = roll;
    def roll1(self):
        print("Roll number is ",self.roll);

class Attributes(Base1,Base2):
    def __init__(self,name,passion,roll):
        Base1.__init__(self , name , passion);
        Base2.__init__(self , roll);

b = Attributes("Ashish","Cricket",44);
b.passion1(),b.roll1();

# Encapsulation
print("================================");

print(" Encapsulation is one of the fundamental concept of OOP in which data is wrapped and this can lead to accidental changes in objects and methods and thus data is wrapped .");


# Polymorphism

# The word Polymorphism means having many forms .In programming a same function can have many forms.This is called polymorphism.

print("================================");
def add(x,y,z=0):
    print(x+y+z);
    print("This is addition of 3 numbers");


add(5,4);
add(1,2,8);

print("================================");


class india:
    def capital(self):
        print("================================");
        print("Country India")
        print("Capital is Delhi");
    def language(self):
        print("National Language is hindi")
    def famouspeople(self):
        print("Chattrapati Shivaji Maharaj");

class usa:
    def capital(self):
        print("================================");
        print("Country America")
        print("Captial is Washington");
    def language(self):
        print("Language is English");
    def famouspeople(self):
        print("George Washington");
        print("================================");

    
i =india();
u = usa();
for country in (i,u):
    country.capital();
    country.language();
    country.famouspeople();

