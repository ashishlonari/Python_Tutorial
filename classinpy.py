
# Class

# If there are no arguments in functions self is compulsory to put inside a function
# So class is user defined blueprint for which objects are specified and can be called wherever required

class dog:
    attr1 ="Mammal"
    attr2 = "4 legs"

    def __init__(self,breed,color):
        self.breed = breed;
        self.color = color;

    def doginfo(self):
        print("The Breed of the dog is :",self.breed);
        print("The Colour of the dog is :",self.color);

    def fun(self):
        print("I am a :",self.attr1);
        print('I have :',self.attr2);

    def __del__(self):
        print("Desctructor is called")
    # Destructor is called at the end of the program.And thus destructor is beign called at the end of statement.

class myname:
    def __init__(self,name):
        self.name = name;
    # So init is used to initialize a attribute in so its a constructor in python
    def say_hi(self):
        print("Owner of the dog shop is ",self.name);

mn = myname("Ashish");
mn.say_hi();
print("======================================")
roger = dog("Indian","black");
tommy = dog("Anerican","White");
tommy.doginfo();
print("======================================")
roger.doginfo();
print("======================================")
print(roger.attr1);
print("======================================")
roger.fun();



