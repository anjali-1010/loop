n=int(input("enter a number"))
s=0
m=n
while n>0:
    d=n%10
    n=n//10
    s=s+d
if m%s==0:
    print(m,"is harshad number")
else:
    print(m,"is not harshad number")