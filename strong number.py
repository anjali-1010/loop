num=int(input("enter a number"))
s=0
tem=num
while(num):
    i=1
    f=1
    r=num%10
    while (i<=r):
        f=f*i
        i=i+1
    s=s+f
    num=num//10
if s==tem:
    print("tha number is strong")
else:
    print("tha number is not strong")

    