#taks
#Q1
"""
factorial
1*2*3*4*5=>120
1*2*3*4*5*6=>720
"""
'''
n=int(input("enter value :"))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial numher :",fact)

#Q2
for i in range(1,11,1):
    print(i)

#Q3
#sum of frist 10 numbers
n=int(input("enther value :"))
s=0
for i in range(1,n+1):
    s+=i
print("sum value :",s)

#Q4
#multiplication table
tbl=int(input("Enter the number :"))
print("multiplication table :",tbl)
for i in range(1,11,1):
    print(i,"x",tbl,"=",i*tbl)
 '''
#Q5
#fibonacci
n=int(input("enther value :"))
n1=0
n2=1
for i in range(n):
    print(n1, end=" ")
    c=n1+n2
    n1=n2
    n2=c


