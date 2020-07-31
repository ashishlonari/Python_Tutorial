# write : this is used to handle the file and used to write on create and write on file
ile = open('ashish.txt','w');
file.write("Hello this is Ashish Lonari")
file.close();

# read:This is used to read the existing file.

file = open('ashish.txt','r');
print(file.read());
file.close();

# append : append the data in text to the existing file
file =open('ashish.txt','a');
file.write("I am Ashish an this text is written again");
file.close();

file =open("ashish.txt",'r');
print(file.read());
file.close()

print("==========================")
# Read and Write : here we can read and write the file at the same time using r+
file = open('ashish.txt','r+');
file.write("Hey guys are you alive");
print(file.read());
file.close();