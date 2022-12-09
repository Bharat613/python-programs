import datetime
f=0
l=0
m=0
print("Enter your date of birth")
x=int(input("Year: "))
y=int(input("Month: "))
z=int(input("Date: "))
g=(datetime.date(x,y,z ))
print()
print("Your DOB:",g)
a=(datetime.datetime.now())
b=str(a)
c=b.split(" ")
e=(c[0])
print("Today's date:",e)
r=e.split("-")
for i in range(x+1,int(r[0])):
    if i%400==0 or (i%4==0 and i%100!=0):
        f=f+366
    else:
        f=f+365
for j in range(y+1,13):
    if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
        l=l+31
    elif j==4 or j==6 or j==9 or j==11:
        l=l+30
    elif j==2:
        if int(x)%400==0 or (x%4==0 and int(x)%100!=0):
            l=l+29
        else:
            l=l+28

o=e.split("-")
for n in range(1,int(o[1])):
    if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
        m=m+31
    elif n==4 or n==6 or n==9 or n==11:
        m=m+30
    elif n==2:
        if int(o[0])%400==0 or (int(o[0])%4==0 and int(o[0])%100!=0):
            m=m+29
        else:
            m=m+28
if y==1 or y==3 or y==5 or y==7 or y==8 or y==10 or y==12:
    p=31-z
elif y==4 or y==6 or y==9 or y==11:
    p=30-z
elif y==2:
    if int(x)%400==0 or (x%4==0 and int(x)%100!=0):
        p=29-z
    else:
        p=28-z
q=o[2]
print()
w=f+l+m+int(p)+int(q)
print(f"You had lived {w} days on this planet")
