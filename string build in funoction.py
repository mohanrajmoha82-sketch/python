#1) .lower()

a="Hello World"
print(a.lower())

#2) .upper()

a="Hello World "
print(a.upper())

#3) .capitalize()
a="Hello World"
print(a.capitalize())

#4) .title()
a="hello i am mohanraj.m full stack developer in hcl."
print(a.title())

#5) .casefold()
a= "Hello I am Mohanraj.M full Stack Developer in Hcl."
print(a.casefold())

#6) .swapcase
a= "i aM fULL sTACK pYTHON developer "
print(a.swapcase())

#7) .center
a="Hello"
#md1
print(a.center(30))
#md2
print(a.center(30,'*'))

#8) .count()
a="mohanraj"
print(a.count('a'))#2
print("naveen".count('a'))#1

#9) .index
a= "Hello world"
print(a.index('o'))#4
print("mohan".index('h'))#2

#10) .rindex
a="Hello World"
print(a.rindex('o'))#7

#11) .find()
a="naveen"
print(a.find('a'))#3


#12) .rfind()
a="mohanraj"
print(a.rfind('a'))
print("naveen".rfind('e'))

#13) .replace
a="hello world"
print(a.replace(" ",'_'))
print("Mohankumar".replace("kumar","Raj"))

#14) .startswith
a="Hello world"
print(a.startswith('H'))#True
print(a.startswith('He'))#True
print(a.startswith('l'))#False

#15) .endswith()
a= "Hello worid"
print(a.endswith('d'))#True
print(a.endswith('id'))#True
print(a.endswith('o'))#False


#16) .format()
a="I am {},my friend name {} working for hcl."
b="mohan"
c="naveen"
print(a.format(b,c))

#17) .encode () and decode()
a= "hello world"
b=a.encode('utf-16')
print(b)
c=b.decode('utf-16')
print(c)

#18) .splitlines
#\n
a="hello\n i am mohan\n am full stack developer\n in hcl"
print(a.splitlines())
#\t
s="hello mohan\tiam naveen\tin python developer."
print(s.splitlines())

#19) .strip() and .lstrip() .rstrip()
a="     mohan     "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

#20 .split()
a="hello world,wellcome to python"
print(a.split())
print(a.split(','))


#21) .translate() and .maketrans()
a="hello world"
t=str.maketrans("hold","3214")
print(a.translate(t))

#22) .zfill()
#1.
a="123"
print(a.zfill(5))
#2.
a="hello"
print(a.zfill(7))

#23) .partition and .rpartition
a="apple-banana-orange"
print(a.partition('-'))
print(a.rpartition('-'))

#24) .islower
a="hello"
print(a.islower())#True
a="Hello"
print(a.islower())#False

#25) .isupper
a="HELLO"
print(a.isupper())#True
b="Hello"
print(b.isupper())#False


#26) .istitle
a="Hello Worid"
print(a.istitle())#True
b="hello Worid"
print(b.istitle())#False


#27) .isalpha
a="HelloWorid"
print(a.isalpha())#True
b="Hello123World@"
print(b.isalpha())#False


#28) .isdigit
a="1234"
print(a.isdigit())#True
b="12He4l6loWorid"
print(b.isdigit())#False

#29) .isalnum()
a="Hello22344556Worid"
print(a.isalnum())#True
b="Hello124Worid#@$5"
print(b.isalnum())#False

#30) .isidentifier()
a="Hello_Worid"
print(a.isidentifier())#True
b="2Helle@#$"
print(b.isidentifier())#False
c="hello_1234world"
print(c.isidentifier())#True

#31) .isasci
a="1232122@moihangghciddccbc"
b="നിങ്ങളുടെ പേരെന്താണ്?"
print(a.isascii())#true
print(b.isascii())#False
