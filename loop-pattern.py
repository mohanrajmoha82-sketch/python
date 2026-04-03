#loop-hollow pattern

n=5

for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
print()
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

#hollow square
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==4 or j==4:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
    

for i in range(n):
    for j in range(n):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#plus pattern

for i in range(n):
    for j in range(n):
        if i==2 or j==2:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if i==2 or j==2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#APPLE
s="APPLE"
for i in range(n):
    for j in range(n):
        if i==2 or j==2:
            print(s[i],end=" ")
        else:
            print(" ",end=" ")
    print()
            

#cross pattern

for i in range(n):
    for j in range(n):
        if i==j or j+i==4:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n):
    for j in range(n):
        if i==j or i+j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#hollow square + Assci pattern
c=90
for i in range(n):
    for j in range(n):
        if i==0 or i==4 or j==0 or j==4:
            print(j,end=" ")
        else:
            print(chr(c),end=" ")
            c-=1
    print()

s="APPLE"
for i in range(n):
    for j in range(n):
        if i==j or i+j==4:
            print(s[i],end=" ")
        else:
            print(" ",end=" ")
    print()

#heif hollow prawid
for i in range(n):
    for j in range(n):
        if i==j or i==4 or j==0:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

#holloe inverted half pyramid
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j+i==4:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()



for i in range(n):
    for j in range(n+4):
        if i==0 or i==j or i+j==8:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n):
    for j in range(n+4):
        if i==j or i==0 or i+j==8:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

