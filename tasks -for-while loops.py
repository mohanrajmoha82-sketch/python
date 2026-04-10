
#q1. palindrome
a=int(input("Enthe the value :"))
b=0
t=a
while t>0:
    d=t%10
    b=b*10+d
    t=t//10
if b==a:
    print(b," is palindrome")
else:
    print(b," is not palindrome")
    

#q2.Armstrome
a=int(input("Enter value  :"))
b=0
t=a
while t>0:
    d=t%10
    b+=d**3
    t=t//10
if b==a:
    print(b," is Armstrom")
else:
    print(b," is not a armstrome")

#Q3. calculate hcf of two given number
#division
a=int(input("Enter value :"))
b=int(input("Enter value :"))
t=0
for i in range(1,a+1):
    if (a%i==0) and (b%i==0):
        hcl=i
print(hcl)

#Q4.
n=50
for i in range (1,n+1):
    if i%3==0 and i%5==0:
        print(i,"hihello")
    elif i%5==0:
        print(i,"hello")
    elif i%3==0:
        print(i,"hi")
    else:
        print(" ")

        
#q5.prime or not
a= int(input("Enter the value :"))
n=0
for i in range(1,a):
    if a%i==0:
        n=n+1
if n==1:
    print(a,"prime number")
else:
    print(a,"not a prime number")
        
#Q6.prime (100)

n=0
for i in range(1,101):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,"prime")
    
#Q7.divison
n=int(input("Enter the valure :"))
for i in range(1,n+1):#12345
    if n%i==0:
        print(i)

#Q8.odd and even
n=int(input("Enter the value :"))
odd=0
even=0
for i in range(1,n+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print(even)
print(odd)

#Q9.perfect square
n=int(input("Enter the velue :"))
j=1
while j<=n:
    print(j,"=",j*j)
    j=j+1

#Q10.spy or hot
"""
a=123
1*2*3=6
1+2+3=6
a=1124
1*1*2*4=8
1+1+2+4=8
"""
a=int(input("Enter the value :"))
b=0
s=1
t=a
while t>0:
    d=t%10
    b=b+d
    s=s*d
    t=t//10
if b==s:
    print(a,"value is spy")
else:
    print(a,"value is not spy")


#Q11.special number
"""
a=29
 2*9   2+9
 18  +  11  =29

"""
a=int(input("Enter the value :"))
b=0
s=0
t=a
while t>0:
    d=t%10
    f=1
    for i in range(1,d+1):#1234
        f*=i
    s+=f
    t=t//10
if s==a:
    print(a,"is a special number")
else:
    print(a,"is not a special ")


#q12.hashad number
"""
a=200
2+0+0=2
200%2=0
"""
a=int(input("Enter the value :"))
b=0
t=a
while t>0:
    d=t%10
    b+=d
    t=t//10
if a%b==0:
    print(a,"is a hashad number")
else:
    print(a,"is not a hashad number")


#Q13.factorial
"""
1*2*3*4*5*6=720
"""
n=int(input("Enter the value :"))
fact=1
for i in range(1,n+1):
    fact*=i
print(n,"Factorial number is",fact)

#Q14.count no of digits
n=int(input("Enter the value :"))
str=str(n)
c=0
for i in str:
    c+=1
print(n,",count the number,",c)

#m2
n=int(input("Enter the value :"))
c=0
while n !=0:
    n=n//10
    c+=1
print(c)

#Q15.squre the digit
#m1
n=int(input("Enter the value :"))
c=0
for i in range(1,n+1):
    j=i**2
    print(j)

#m2
n=int(input("Enter the value :"))
i=0
while n>0:
    a=n**2
    print(a)
    n-=1
    
   




























    
    
