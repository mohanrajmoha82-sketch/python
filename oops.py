#opps
"""
syntax of class and object
class class_name:
    #set of attributes and functions

syntax of constructor
 class class_name:
    def___init___(seif):
      //block of code
"""
class Mobile:
    brand= None
    model= None
    color= None
    price= None
    def button(self):
        print(self.brand,"Button help's to mobile on/off")
        print("END".center(30,"*"))

m1=Mobile()
m1.brand = "Samsung"
m1.model = "S24"
m1.color = "black"
m1.price = "₹100000"
print("mobile brand: ",m1.brand)
print("mobile model: ",m1.model)
print("mobile color: ",m1.color)
print("mobile price: ",m1.price)
m1.button()

m2 = Mobile()
m2.brand = "one plus"
m2.color = "black"
m2.model = "CE3"
m2.price ="12000"
print("mobile brand: ",m2.brand)
print("mobile model: ",m2.model)
print("mobile brand: ",m2.color)
print("mobile color: ",m2.price)
m2.button()


# tasks
# Q1) laptop
class Laptop:
    brand = None
    model = None
    color = None
    price = None
    def button(self):
        print("END".center(30, "*"))
l1=Laptop()
l1.brand = "Lenovo"
l1.model = "Lenovo LOQ 15iAX9"
l1.color = "Luna Grey"
l1.price = 55000
print("Laptop brand: ",l1.brand)
print("Laptop model: ",l1.model)
print("Laptop color: ",l1.color)
print("Laptop price: ",l1.price)
l1.button()
l2=Laptop()
l2.brand = "ASUS"
l2.model = "Vivobook Go 15"
l2.color = "Green"
l2.price = 48990
print("Laptop brand: ",l2.brand)
print("Laptop model: ",l2.model)
print("Laptop color: ",l2.color)
print("Laptop price: ",l2.price)
l2.button()




# Q2)Student
# constructor function
class student:
    id = None
    name = None
    mark = None
    def __init__(self,id,name,mark):
        self.id = id
        self.name = name
        self.mark = mark
        print("student id: ",self.id)
        print("student name: ",self.name)
        print("student mark: ",self.mark)
        print("END".center(30,"*"))
s1=student("444 111 45","mohan",60)


#class and object
class student:
    id = None
    name = None
    mark = None
    def id1(self):
        print("END".center(30,"*"))
s1=student()
s1.id="444 111 45"
s1.name="mohan"
s1.mark=60
print("Student id",s1.id)
print("Student name",s1.name)
print("Student mark",s1.mark)
s1.id1()

# Q3) fan
class fan:
    def method(self):
        print("Fan switch on /off")
f1= fan()
f1.method()

# Q4)book
class Book:
    name=None
    Author=None
    price=None
    def create(self):
        print("creating book")
        print("END".center(50,"*"))
B1=Book()
B1.name="The Alchemist"
B1.Author="Paulo Coelho"
B1.price="₹100"
print("Book Name:",B1.name)
print("Book Author:",B1.Author)
print("Book Price:",B1.price)
B1.create()

B2=Book()
B2.name="The Kite Runner"
B2.Author="Khaled Hosseini"
B2.price="₹199"
print("Book Name:",B2.name)
print("Book Author:",B2.Author)
print("Book Price:",B2.price)
B2.create()

B3=Book()
B3.name="To Kill A Mockingbird"
B3.Author="Harper Lee"
B3.price="₹419"
print("Book Name:",B3.name)
print("Book Author:",B3.Author)
print("Book Price:",B3.price)
B3.create()

class Book:
    name=None
    Author=None
    price=None
    def __init__(self,name,Author,price):
        self.name=name
        self.Author=Author
        self.price=price
        print("Book Name",self.name)
        print("Book Author",self.Author)
        print("Book Price",self.price)
        print("END".center(50,"*"))
B1=Book("The Alchemist","Paulo Coelho","₹100")
B2=Book("The Kite Runner","Khaled Hosseini","₹199")
B3=Book("To Kill A Mockingbird","Harper Lee","₹419")

# Q5)bike
class Bike:
    def ride(self):
        print("The bike is riding")
b=Bike()
b.ride()

# Q6)Employee
class Employee:
    id=None
    name=None
    salary=None
    def company(self):
        print("END".center(30,"*"))
e1=Employee()
e1.id=101
e1.name="naga raj"
e1.salary=100000
print("name: ",e1.name)
print("naga raj id: ",e1.id)
print("naga raj salary: ",e1.salary)
e1.company()

class Employee:
    id=None
    name=None
    salary=None
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
        print("ID:",self.id)
        print("name:",self.name)
        print("salary:",self.salary)
        print("END".center(30,"*"))
e1=Employee(101,"naga raj",100000)


# Q7) mobile
class mobile:
    def calling(self):
        print("Mobile calling...")
m=mobile()
m.calling()

# Q8)Hospital
class Hospital:
    hospital_name = None
    doctor_name = None
    location = None
    def method(self):
        print("END".center(30,"*"))
h1=Hospital()
h1.hospital_name = "mohan hospital"
h1.doctor_name = "Dc.Naveen"
h1.location =("salem")
print("Hospital Name: ",h1.hospital_name)
print("Doctor name: ",h1.doctor_name)
print("location: ",h1.location)
h1.method()


class Hospital:
    def __init__(self,hospital_name,doctor_name,location):
        self.hospital_name = hospital_name
        self.doctor_name = doctor_name
        self.location = location
        print("Hospital Name: ",self.hospital_name)
        print("Doctor name: ",self.doctor_name)
        print("Location: ",self.location)
        print("END".center(30,"*"))
h1=Hospital("mohan hospital","DC.naveen","salem")

#constructor Question
#Q9) car
class Car:
    brand=None
    model=None
    color=None
    price= None
    def __init__(self,brand,model,color,price):
        brand=brand
        model=model
        color=color
        price=price
        print("Car brand name: ",brand)
        print("Car model: ",model)
        print("Car color: ",color)
        print("Car prince: ",price)
c1=Car("Mahindra","AXT2WD","black","9.99lakh")

#Q10) Movie
class Movie:
    title=None
    director=None
    year=None
    def __init__(self,title,director,year):
        title=title
        director=director
        year=year
        print("Movie Title: ",title)
        print("Movie director: ",director)
        print("Movie Release Year: ",year)
        print("END".center(30,"*"))
m1=Movie("Jana Nayagan","H.Vinoth","2026")
m2=Movie("meesaya murukku 2","Hiphop Tamizha Adhi","2026")

#Q11) Teacher
class Teacher:
    name=None
    subject=None
    experience=None
    def __init__(self,name,subject,experience):
        name=name
        subject=subject
        experience=experience
        print("Teacher Name: ",name)
        print("subject: ",subject)
        print("experience: ",experience,"years")
        print("End".center(30,"*"))
t1=Teacher("Praveen","Python","5")
t2=Teacher("Naveen","AI","4")

#Q12)Bank
class Bank:
    name=None
    bankno=None
    balance=None
    def __init__(self,name,bankno,balance):
        name=name
        bankno=bankno
        balance=balance
        print("Your name: ",name)
        print("Bank number: ",bankno)
        print("pin number: ",balance)
        print("END".center(30,"*"))
b1=Bank("Mohanraj","987654567","12340")
b2=Bank("Naja Raj","877654493","12346780")

#Q13) Rectangle
class Rectangle:
    l=None
    w=None
    def __init__(self,l,w):
        A=l*w
        print(f"if length is {l} width is {w} the Rectangle area is {A}")
r1=Rectangle(l=10,w=20)
r1=Rectangle(10,5)

import math
#Q14) Circle
class Circle:
    r=None
    def __init__(self,r):
        A=(math.pi)*r**2
        print("The Cricle area is approximately",A,)
c1=Circle(7)
c2=Circle(8)

#Q15) College
class College:
    name=None
    couse=None
    location=None
    student_count=None
    def __init__(self,name,couse,location,student_count):
        name=name
        couse=couse
        location=location
        student_count=student_count
        print("College Name: ",name)
        print("College couse: ",couse)
        print("College location: ",location)
        print("College Student count",student_count)
        print("END".center(30,"*"))
c1=College("AVS","Bsc,BA,BE,B.com,B.com(CA)","Salem","1200")
c2=College("ABC","MSC,MBA,PHT,M.Com","Erode","1560")

#Inheritance
#single level Inheritance
class Book:
    name="Learn python"
    def fun1(self):
        print(f"Book Name: {self.name}")
class Author(Book):
    author="Naveen"
    def fun2(self):
        print(f"Author Name: {self.author}")
a=Author()
print(a.name)
print(a.author)
a.fun1()
a.fun2()

#multi level Inheritance
class Book:
    name="Learn python"
    def fun1(self):
        print(f"Book Name: {self.name}")
class Author(Book):
    author="Naveen"
    def fun2(self):
        print(f"Author Name: {self.author}")
class Book_price(Author):
    def fun3(self):
        print("Book price Rs: 100")
g=Book_price()
g.fun1()
g.fun2()
g.fun3()

#Hierachical
class Upi:
    def Upi_money_transfor(self):
        print("UPI money trunsfor System")
class Gpay(Upi):
    def gpay_access(self):
        print("Gpay  user Account Access")
class Phonepy(Upi):
    def phonepy_access(self):
        print("PhonePy user Account Access")
class Pytem(Upi):
    def pytem_access(self):
        print("Pytem user Account Access")
pt=Pytem()
pt.pytem_access()
pt.Upi_money_transfor()
gp=Gpay()
gp.gpay_access()
gp.Upi_money_transfor()


#multiple
class Camera:
    def camera_access(self):
        print("Camera take good photo")
class Radio:
    def radio_access(self):
        print("Play the good songs")
class Tv:
    def tv_access(self):
        print("Warch the good movies")
class Smartphone(Camera,Radio,Tv):
    def smartphone_access(self):
        print("Enjoy the with friend via calling and internet")
sm=Smartphone()
sm.tv_access()
sm.smartphone_access()
sm.camera_access()
sm.radio_access()