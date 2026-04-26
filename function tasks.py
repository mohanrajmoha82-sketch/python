#positional argument or required argument
#from curses.ascii import isupper
#from curses.ascii import isupper


def add(x,y):
    a=x
    b=y
    c=a+b
    print("add :",c)
# add(30,60)
# add(20,25)

#2.default argument
def full_name(fn="mohan",ln="raj"):
    print(fn+" "+ln)
full_name()
full_name("suresh","kumar")
# full_name("naveen","kumar")


#keyword argument
def info(**d):
    print(d)
    print(type(d))
    for i,j in d.items():
        print(i,":",j)
#info(Brand="samgung",model="s25",price=80000,coloe="black")


#variable argument
def student(*n):
    print(n)
    print(type(n))
    for i in n:
        print(i)
#student("naveen","mohan","naga raj","pradeepa","aarthi","barathi")

#tasks
#1.)
def s():
    for i in range(1,11,1):
        print(i*2)
#s()

#2)
def s1():
    for i in range(50,-1,-10):
        if i==0:
            print(i)
        else:
            print(i,end=" ")
#s1()

#3) square
def square(a):
    for i in range(1,11,1):
        print(i**a)
#square(2)

#4)
def split_digits(n):
    a=n[::-1]
    print(a)
#split_digits("4327")

#5) cube
def cube(b):
    a=b**3
    print(f" cube={b},  value={a}")
#cube(4)

#6) armstrong number
def armstrong(n):
    b=0
    t=n
    while t>0:
        d=t%10
        b+=d**3
        t=t//10
    if b==n:
        print(f"{n} ia an armstrong number...")
    else:
        print(f"{n} is not a armstrong number...")
#armstrong(153)

#7) spy
def spy(n):
    a=0
    b=1
    t=a
    while t>0:
        d=t%10
        a=a+d
        b=b*d
        t=t//10
    if a==b:
        print(f"{n} ia an spy number...")
    else:
        print(f"{n} is not a spy number...")
#spy(123)


#8) square of  each digits in the number
def digits(n):
    a=str(n)
    s = a[::-1]
    for i in s:
        if i.isdigit():
            b=int(i)
            c=b**2
            print(c,end=" ")
#digits(42316)

#9) count the function
def count_digits(n):
    a=str(n)
    print(len(a))
#count_digits(34562)

#10) sum
def value(a,b):
    c=a+b
    print(c)
value(5,6.1)

11) calculate discount
price=int(input("enter price:"))
def calculate_charg(price):
    if price >= 50000:
        b = price*10/100
        c = price - b
        print(c)
    elif price >=30000 and price <= 49999:
        b = price * 5 / 100
        c = price - b
        print(c)
    else:
        b = price * 2 / 100
        c = price - b
        print(c)
calculate_charg(price)


#12)checksif a character is a capital letter
##md1
def capital(ch):
    print(ch.isupper())
#capital("MOHAN")

#md2-lambfda
capital =lambda ch:ch.isupper()
#print(capital("NAVEEN"))

#md3-return
def capital(ch):
    return ch.isupper()
a=capital("NAGARAJ")
#print(a)

#13)vowels or consonant
word=input("enter the word :")
def letter(world):
    vowel="aeiouAEIOU"
    if world in vowel:
        print("vowel...")
    else:
        print("consonaat...")
#letter(word)

#14)checks the lowercase
#md1
def lowercase(ch):
    print(ch.islower())
#lowercase("nagaraj")

#md2-lambda
character=lambda ch:ch.islower()
#print(character("naveen"))

#md3-return
def character(ch):
    return ch.islower()
a=character("mohan")
print(a)



