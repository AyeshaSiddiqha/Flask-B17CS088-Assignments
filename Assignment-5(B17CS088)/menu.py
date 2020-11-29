import re
import bcrypt
import json
import math, random
import smtplib

user={}
flag=flag1=flag2=1
print("Welcome")
print("select an option:")
print("1.Sign Up")
print("2.Sign In")
x=int(input())
if x==1 :

    while flag==1:
        print("Enter correct email:")
        e1=input()
        z=re.match(r"\S+@gmail\S+",e1)
        if z:
            flag=0
    while flag1==1:
        print("Enter Strong password:")
        p1=input()
        y= re.match(r"^[A-Za-z0-9#@&$*%!]{7,}$", p1)
        if y:
            flag1=0
    if y:
        #print("good password")
        p=p1.encode('utf-8')
        hashval1=bcrypt.hashpw(p,bcrypt.gensalt())
        #print(hashval1)
        if bcrypt.checkpw(p,hashval1):
            print("pswd hashed")
        else:
            print("pswd hashing unsuccessful")
    if z:
        #print("correct email format")
        e=e1.encode('utf-8')
        hashval2=bcrypt.hashpw(e,bcrypt.gensalt())
        #print(hashval2)
        if bcrypt.checkpw(e,hashval2):
            print("email hashed")
        else:
            print("email hashing unsuccessful")

#OTP  
    digits = "0123456789"
    OTP = "" 
    for _ in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 

    if z:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        f=open('C:/Users/azhar/Documents/first/pswd.txt').read()
        s.login("ayeshasiddiqha234@gmail.com", f)
        msg='Your OTP for Verification is '+OTP
        s.sendmail('ayeshasiddiqha234@gmail.com',e1,msg)

    print("enter received otp ")
    while flag2==1:
        v=int(input())
        if v==int(OTP):
            user[e1]=p1
            json_object=json.dumps(user)
            #print(json_object)
            with open('person.json','w') as f:
                f.write(json_object)
            print("Congratulations!!...Account Created.")
            flag2=0
        else:
            print("Incorrect OTP...try again")

if x==2:
    print("Enter your email:")
    e2=input()
    print("Enter your password:")
    p2=input()
    with open('person.json') as f:
        data=json.load(f)
    if data[e2]==p2:
        print("successful sign in")
    else:
        print("Incorrect Data")

