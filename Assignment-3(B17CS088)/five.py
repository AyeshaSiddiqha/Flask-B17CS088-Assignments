import re
f=open('C:/Users/azhar/Desktop/data.txt','r')
f2=open('new.txt',"w")
d=f.read()
name=re.compile(r"(^[A-Z][a-z]+)\s([A-Z][a-z]+)")
phn=re.compile(r"[+\d+]")
email=re.compile(r'\S+@gmail\S+')
phn1=phn.finditer(d)
print("phone numbers: ")
for match in phn1:
    print(match.group())
names=name.finditer(d)
print("names: ")
for match in names:
    print(match.group())
emails=email.finditer(d)
print("emails: ")
for match in emails:
    print(match.group())
f.close()
x=open('data.txt','r')
z=x.sub('Dave','John',f2)
print(z)
f.close()
