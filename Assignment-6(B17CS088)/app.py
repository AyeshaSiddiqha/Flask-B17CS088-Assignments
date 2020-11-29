from flask import Flask,request,render_template
import re
import bcrypt
import json
import math, random
import smtplib

digits = "0123456789"
OTP = ""
for _ in range(4) : 
   OTP += digits[math.floor(random.random() * 10)]
o1=OTP.encode('utf-8')
hasho1=bcrypt.hashpw(o1,bcrypt.gensalt())

app=Flask(__name__)
 
@app.route("/")
def form():
    return render_template('login.html')

@app.route("/signin",methods=['POST'])
def signin():
   return render_template('signin.html')

@app.route("/postsignin",methods=['POST'])
def success():
   e2=request.form['email_id']
   p2=request.form['password']
   p3=p2.encode('utf-8')
   with open('person.json','r') as f:
      data=json.load(f)
   if data['Email']==e2 :
      t=data['Password']
      u=t.encode('utf-8')
      if bcrypt.checkpw(p3,u):
         return "Signin Successful"
      else:
         return "Failed to sign in"

@app.route("/forgotpass",methods=['POST'])
def forgotpass():
   s = smtplib.SMTP('smtp.gmail.com', 587)
   s.starttls()
   f=open('C:/Users/azhar/Documents/Chubb/2/first/pswd.txt').read()
   s.login("ayeshasiddiqha234@gmail.com", f)
   msg='Your OTP for Password reset is '+OTP
   s.sendmail('ayeshasiddiqha234@gmail.com',request.form['email_id'],msg)
   return render_template('forgot.html')

@app.route("/passvalidate",methods=['POST'])
def passvalidate():
   o2=request.form['otp']
   if o2==OTP:
      return render_template('resetpass.html')
   else:
      return "Incorrect OTP"

@app.route("/resetsuccess",methods=['POST'])
def resetsuccess():
      p1=request.form['password']
      p=p1.encode('utf-8')
      hashp1=bcrypt.hashpw(p,bcrypt.gensalt())
      with open('person.json', 'r') as f:
         test_dict = json.load(f)
      test_dict.update({'Password':hashp1.decode()})
      y=json.dumps(test_dict)
      with open('person.json','wb') as f:
         f.write(y.encode())
         return "Account reset Successful"

@app.route("/signup",methods=['POST'])
def signup():
   return render_template('signup.html')

@app.route("/otp",methods=['POST'])
def otp():
   e1=request.form['email_id']
   p1=request.form['password']
   p=p1.encode('utf-8')
   hashp1=bcrypt.hashpw(p,bcrypt.gensalt())
   user={'Email':e1,'Password':hashp1.decode(),'OTPGEN':hasho1.decode()}
   x=json.dumps(user)
   with open('person.json','wb') as f:
      f.write(x.encode())
   s = smtplib.SMTP('smtp.gmail.com', 587)
   s.starttls()
   f=open('C:/Users/azhar/Documents/Chubb/2/first/pswd.txt').read()
   s.login("ayeshasiddiqha234@gmail.com", f)
   msg='Your OTP for Verification is '+OTP
   s.sendmail('ayeshasiddiqha234@gmail.com',request.form['email_id'],msg)
   return render_template('otp.html')

@app.route("/validate",methods=['POST'])
def validate():
   o2=request.form['otp']
   o3=o2.encode('utf-8')
   if bcrypt.checkpw(o3,hasho1):
      with open('person.json', 'r') as f:
         test_dict = json.load(f)
      new_dict = {key:val for key, val in test_dict.items() if key != 'OTPGEN'}
      x=json.dumps(new_dict)
      with open('person.json','w') as f:
         f.write(x)
         return "Account Created successfully"
   else:
      return "Incorrect otp"





if __name__=="__main__":
    app.run(debug =True)