# Why we use Regular Expression?
# For example if we want to remove a letter from a string it would be tedious task to remove the letter as we have to manipilate the string and apply for loops but with regular expression it is very easy.

import re

mystr = ''' TCS is the second largest Indian company by market capitalisation.[9][10] Tata consultancy services is now placed among the most valuable IT services brands worldwide.[11] In 2015, TCS was ranked 64th overall in the Forbes World's Most Innovative Companies ranking, making it both the highest-ranked IT services company and the top Indian company.[12] It is the world's largest IT services provider.[13] As of 2018, it is ranked eleventh on the Fortune India 500 list.[14] In April 2018, TCS became the first Indian IT company to reach $100 billion in market capitalisation,[15] and second Indian company ever (after Reliance Industries achieved it in 2007)[16] after its market capitalisation stood at ₹6,79,332.81 crore ($102.6 billion) on the Bombay Stock Exchange.[17][18][19] '''

p = re.compile('comp');
match = p.finditer(mystr);
for m in match: 
    print(m)
# So we use to find this to find "comp" in the word so we get the output were words with comp are in output.

print("=========================");

# Here one or more occurence of 're' in 're+'  
c = re.compile('re+');
# In re* there is any number of occurunces including 0 in re*
d = re.compile('re*');
w = c.finditer(mystr);
v = d.finditer(mystr);
for s in w:
    print(s);
print("======================")
for p in v:
    print(p); 
print("======================")

# Here findall is used to find all the elements from a to e in a string str2 
# []
str2="a Ashish is pursuing Engineering at Modern College";
s = re.compile('[a-e]');
j=s.findall(str2);
print(j);

print("======================")

# By doing this we get if number of i s are greater or equal to 2 it will print it.
str3="aiaaiii i am a good aiaiall is well ai";
airep = re.compile('ai{2}');
repeat=airep.finditer(str3);
for lu in repeat:
    print(lu);

print("======================")

# Now if we want ai in group and ai repeates twice or more we use round brackets.
str4="aiaaiii i am a good aiaiall is well ai";
airep = re.compile('(ai){2}');
repeat=airep.finditer(str3);
for lu in repeat:
    print(lu);
print("======================")

# now if we want an or thai is for ex: 'll' or 'ai' then we use '|'
# Or function in regular expression

str5="aiaaiii i am a good aiaiall is well ai";
rc=re.compile('ai|ll');
a=rc.findall(str5);
print(a);
print("==============================")

# \A returns a match if the specified character are at the beginning of the string.

str5="aiaaiii i am a good aiaiallaia is well aiaia";
rc=re.compile('\Aaia');
a=rc.finditer(str5);
for i in a:
    print(i);
print("==============================")

# \b returns a match if the specified character are at the beginning of the string or at the end of the string.

str6="aiaaiii i am a good aiaiallaia is well laia";
rc1=re.compile('\baia');
a2=rc1.finditer(str6);
for i in a2:
    print(i);
print("==============================")

# \d Now idf therae are lots of number which have 5 digits at start then - and 5 digits at the end so we can get the match by using '\d'

# {} curly braces are used to specify exactly the number of occurunces

str7="aiaaiiimob no . : 98230-19305  97652-59595 a good aiaiallaia is well aiaia";
rc=re.compile('\d{5}-\d{5}');
a=rc.finditer(str7);
for i in a:
    print(i);
print("==============================")


