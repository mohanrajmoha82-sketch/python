#if

b=int(input("Enter the values :"))
if b == 0:
    print(b,"is zero")


#if-else

m=int(input("Enter M value :"))#50
n=int(input("Enter N value : "))#20
if m>n:
    print("qustion :",m//n)
    print("Remainder :",m%n)
else:
    print("N is greaterthan m...")


#3

b=int(input("Enter the value :"))
if (b%2)== 0:
     print(b,"is even number")
else:
    print(b,"is not even number...")
    
#4.
"""
find the vawels sound(AEIOU)
(AEIOU)the litter is true statement
more litter flase statement
"""
c=input("enter the letter (AtoZ) :")
if c=="A" or c=="E" or c=="I" or c=="O" or c=="U":
    print(c, "is vowels sound")
else:
    print(c, "is not vowela sount")

#syntax of if-elif-else
# find the grade of studants based pn avarage

"""
100-90 -->A+
89-80 --->A
79-70 --->B+
69-60 --->B
avg<60 ---> fail
"""
T=int(input("Tamil mark :"))#75
E=int(input("english mark :"))#45
M=int(input("Maths mark :"))#67
S=int(input("Sic mark :"))#78
SS=int(input("SS :"))#50

total_mark=T+E+M+S+SS
avg=total_mark/5
print("avg :",avg)
if avg<=100 and avg>=90:
    print("A+ grade")
elif avg<90 and avg>=80:
    print("A grade")
elif avg<80 and avg>=70:
    print("B+ grade")
elif avg<70 and avg>=60:
    print("B grade")
else:
    print("student is fail")

#nested if

email=input("Enter the email :")
if email == "abc123@gmail.com":

    pas=int(input("Enter the LPassword"))
    if pas == 12345:
        print("login sucess")
    else:
        print("worng password")
else:
    print("Invaild Email Id")


#taks
#Q1

m=int(input("Enter M value :"))#50
n=int(input("Enter N value : "))#20
if m>n:
    print("qustion :",m//n)
    print("Remainder :",m%n)
else:
    print("N is greaterthan m...")


#Q2
#positive and negative

a=int(input("Enter the number :"))
if a>0:
    print(a,"is positive volue...")
else:
    print(a,"is negative volue...")

#odd or even
a=int(input("Enter the number :"))
if (a%-2)==0:
    print(a,"this number even...")
else:
    print(a,"this number obb")

#pass or fail

Mark=int(input("Enter the mark :"))
if Mark<=100 and Mark>=50:
    print("this mark pass")
else:
    print("this mark fail")
    

#leap year

year=int(input("Enther the year :"))
if year%4==0:
    print(year,"this year leap year...")
elif year%100==0:
    print(year,"this year leap year...")
elif year%400==0:
    print(year,"this year leap year...")
else:
    print(year,"this not year leap year...")


#Q4
#vowels and consonants

a=input("enther the letter (AtoZ) :")
if a=="A" or a=="E" or a=="I" or a=="O" or a=="U":
    print(a,"this litter is vowels...")
else:
    print(a,"this litter is consonants...")

#Q5

"""
max and min
max-hig , min-small
"""
a=int(input("enter A number :"))
b=int(input("enter B number :"))
c=int(input("enter C number :"))
print("max number...")
if a>=b and a>=c:
    print("max number :",a)
elif b>=a and b>=c:
    print("max number :",b)
else:
    print("max number :",c)
print("min number...")
if a<=b and a<=c:
    print("min number:",a)
elif b<=a and b<=c:
    print("min number :",b)
else:
    print("min number : ",c)


#Q6
"""
winter: Dec 20 - Mar 15
spring: Mar 16 - Jun 25
summer: Jun 26 - Sep 19
Autumn: Sep 20 - Dec 19
"""
month=int(input("Enther the month(1-12) :"))
day=int(input("Enter the day (1-31) :"))
if (month==12 and day>=20) or (month==3 and day<=15):
    print("Month :",month,"Day :",day,"Winter season")
elif (month==3 and day>=16) or (month==6 and day<=25):
    print("Month :",month,"Day :",day,"Spring season")
elif (month==6 and day>=26) or (month==9 and day<=19):
    print("Month :",month,"Day :",day,"Summer season")
else:
    print("Month :",month,"Day :",day,"Autumn season")
    


#Q7

month=input("Enter the Month :")
if month=="january" or month=="March" or month=="May" or month=="July" or month=="Augist" or month=="October" or month=="December":
     print(month,"31 days")
elif month=="Apirl" or month=="June" or month=="September" or month=="November":
    print(month,"30 days")
else:
    print(month,"28 or 29 days")
 

#Q8

n=int(input("Enter the number :"))
if n%5==0:
    print("Hello")
else:
    print("Bye")


#Q9

tem=int(input("Enter the temperture of celsius :"))
if tem>=100:
    print(tem,"boilling")
else:
    print(tem,"not boilling")


#Q10

days=int(input("Enter the number of day :"))

if days<=5:
    print(days,"day Charge",days*2)
elif days<=10:
    print(days,"day Charge",days*3)
elif days<=15:
    print(days,"day Charge",days*4)
else:
    print(days,"day Charge",days*5)


#Q13

#first 100 units-->1.5
#next 200 units-->2.5
#above 200 unita-->4
units=int(input("enther the units :"))
if units<=100:
    print("electric bill :",units*1.5)
elif units<=200:
    print("electric bill :",units*2.5)
else:
    print("electric bill :",units*4)
    


#Q14

email=input("Enter the Email :")
if email=="abc@gmail.com":
    pas=int(input("Enter the password :"))
    if pas==12345:
        print("password is right...")
    else:
        print("check the password...")
else:
    print("check the Email...!")

            
            




























 
