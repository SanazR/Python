import re

#To find out if the texts are match the pattern.

text="random string ,myname1@gmail.com, 1542 abcdefg, mani_16@mycompany.net"
pattern=re.compile("[ABCa]")
#looking for single letterswhich either,A,B or C

result=pattern.search(text)
print(result)

#the result just shows m because the search funct just look for the first match and stops after finds the first match.

pattern=re.compile("[a-zA-Z0-9]+")
#the "+"means one or more letters

result=pattern.search(text)
print(result)

#We seprated email from the rest of the text
pattern=re.compile("[a-zA-Z0-9.-_]+@[a-zA-Z0-9]+.[a-zA-Z]+")
#the "+"means one or more letters
#\. means just print ".". However, apparently in the new py version there is no need for \

result=pattern.search(text)
print(result)

result=pattern.findall(text) 
#to find both emails
print(result)